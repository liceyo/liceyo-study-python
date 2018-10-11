# 题目：求输入数字的平方，如果平方运算后小于 50 则退出。

again = True
while again:
    n = float(input("num:"))
    s = n * n
    print("number:%d,sqrt:%d" % (n, s))
    if s < 50:
        again = False
