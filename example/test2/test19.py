"""
题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。
例如6=1＋2＋3.编程找出1000以内的所有完数。
"""

for n in range(1, 10000):
    c = []
    k = 0
    for y in range(1, n):
        if n % y == 0:
            c.append(y)
            k += y
    if k == n:
        print("完数：%4ld" % n, c)
