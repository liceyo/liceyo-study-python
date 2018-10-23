
# 题目：找到年龄最大的人，并输出。

import operator

person = {"li":18,"wang":50,"zhang":20,"sun":22}
print(max(person.items(), key=operator.itemgetter(1))[0])    # 获取最大值的 key
print(max(person.values()))    # 获取最大值