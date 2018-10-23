# 查询
import re

import escfg
import query_functions

es_client = escfg.es_client
# 内容，标题基础加权参数
_disease_name_base_weight = [1, 2]


# 分词
def token(q: str):
    q_analyze_result = es_client.indices.analyze(
        index='hsgene_ai',
        body={
            "analyzer": "ik_smart",
            "text": "%s" % q
        }
    )
    return [t['token'] for t in q_analyze_result['tokens'] if t['type'] != 'OTHER_CJK']


# 加权
def weight(tokens):
    words = [[t, 7, 5] for t in tokens]
    disease_name_weight(words)
    return words


# 疾病名加权
def disease_name_weight(words):
    tokens = [word[0] for word in words]
    disease_response = es_client.search(
        index='hsgene_ai',
        body={
            "_source": {
                "includes": [
                    "disease_name_en",
                    "disease_name_cn"
                ]
            },
            "query": {
                "bool": {
                    "should": [
                        {
                            "terms": {
                                "disease_name_en": tokens
                            }
                        },
                        {
                            "terms": {
                                "disease_name_cn": tokens
                            }
                        }
                    ]
                }
            }
        }
    )
    names = set()
    for hit in disease_response['hits']['hits']:
        d = hit['_source']
        if d.get('disease_name_en') is not None:
            names.add(d['disease_name_en'])
        if d.get('disease_name_cn') is not None:
            names.add(d['disease_name_cn'])
    for i in range(len(words)):
        if words[i][0] in names:
            words[i][1] += _disease_name_base_weight[0]
            words[i][2] += _disease_name_base_weight[1]


# 构建基础查询
def build_base_query(words):
    base_query = []
    for word in words:
        base_query.append({
            "constant_score": {
                "filter": {
                    "term": {
                        "search_title": {
                            "value": word[0]
                        }
                    }
                },
                "boost": word[1]
            }
        })
        base_query.append({
            "constant_score": {
                "filter": {
                    "term": {
                        "search_body": {
                            "value": word[0]
                        }
                    }
                },
                "boost": word[2]
            }
        })
    return {"bool": {"should": base_query}}


# 构建函数查询
def build_function_query(types: list):
    function_query = [query_functions.show_count_function]
    if 'dcw' in types:
        function_query.append(query_functions.index_function)
        function_query.append(query_functions.good_count_function)


# 构建查询
def build_query(q: str, types: list):
    tokens = token(q)
    words = weight(tokens)
    return {
        'function_score': {
            "query": build_base_query(words),
            "functions": build_function_query(types),
            "score_mode": "sum",
            "boost_mode": "sum",
            "max_boost": 1000
        }
    }


# 构建高亮查询
def build_highlight(q: str, types: list, pre_tag="<em class='strong'>", post_tag="</em>"):
    q_highlight = '(' + re.sub(re.compile('\\s+'), ')(', q.strip()) + ')'
    fields = {}
    highlight_fields = set()
    for t in types:
        tp = escfg.modules.get(t)
        if tp is not None:
            for hf in tp['highlight']:
                highlight_fields.add(hf)
    for hf in highlight_fields:
        if hf == 'search_body':
            fields[hf] = {
                "fragment_size": 120,
                "number_of_fragments": 3
            }
        else:
            fields[hf] = {
                "number_of_fragments": 0
            }
    return {
        "pre_tags": [pre_tag],
        "post_tags": [post_tag],
        "type": "fvh",
        "highlight_query": {
            "query_string": {
                "query": q_highlight,
                "fields": list(highlight_fields),
                "analyzer": "ik_smart"
            }
        },
        "require_field_match": False,
        "fields": fields
    }


def builder(q: str, types: list):
    includes = set()
    for t in types:
        tp = escfg.modules.get(t)
        if tp is not None:
            for ic in tp['include']:
                includes.add(ic)
    return {
        "from": 0,
        "size": 11,
        "query": build_query(q, types),
        "post_filter": {
            "terms": {
                "dataType": types
            }
        },
        "_source": {
            "includes": list(includes)
        },
        "highlight": build_highlight(q, types)
    }


def query(q: str, types: list):
    qs = builder(q, ["article"])
    return es_client.search(index='hsgene_ai', body=qs)


if __name__ == '__main__':
    q = '人群越来越高发'
    response = query(q, ['article', 'research'])
    for hit in response['hits']['hits']:
        print(hit['_score'])
        print(hit['_source'])
        print(hit['highlight'])
