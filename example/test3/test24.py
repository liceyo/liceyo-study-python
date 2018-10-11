# 题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。

a = 1.0
b = 1.0
cnt = 0.0
for i in range(20):
    a, b = a + b, a
    cnt += float(a / b)
    print("%d/%d:count=%f" % (a, b,cnt))
