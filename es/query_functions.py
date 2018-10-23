# 浏览量函数
show_count_function = {
    "filter": {
        "match_all": {
            "boost": 1
        }
    },
    "field_value_factor": {
        "field": "show_count",
        "factor": 0.007,
        "missing": 0,
        "modifier": "log1p"
    }
}
# 点赞数函数
good_count_function = {
    "filter": {
        "term": {
            "dataType": {
                "value": "dcw",
                "boost": 1
            }
        }
    },
    "field_value_factor": {
        "field": "user_evaluate.good_count",
        "factor": 0.01,
        "missing": 0,
        "modifier": "log1p"
    }
}
# 神灯指数函数
index_function = {
    "filter": {
        "term": {
            "dataType": {
                "value": "dcw",
                "boost": 1
            }
        }
    },
    "field_value_factor": {
        "field": "index_totalIndex",
        "factor": 0.07,
        "missing": 0,
        "modifier": "square"
    }
}
