# --elasticsearch 配置
# -集群信息
from elasticsearch import Elasticsearch

cluster = ['172.30.10.160:9200']
# -索引名称
index_name='hsgene_ai'
# -索引类型
index_type='hsgene_type'
# -模块搜索必含字段
module_must_include=["id","search_body","dataType","show_count"]
# -全部搜索包含模块
module_whole_search=["article","research"]
# -模块信息
modules = {
    "article": {
        "highlight": ["search_body","title"],
        "include":module_must_include+["title","create_date_time","icon","category_name"]
    },
    "research":{
        "highlight": ["search_body","scientific_research_title"],
        "include":module_must_include+["scientific_research_title","date_time","source","author","magazine"]
    }
}

es_client=Elasticsearch(cluster)