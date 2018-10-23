"""
题目：有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。
"""

if __name__ == '__main__':
    n = 8
    num = [i+1 for i in range(n)]
    print(num)
    k = 0
    i = 0
    r = 0
    while n > 1:
        if num[i] != 0:
            k = k+1
        if k == 3:
            n -= 1
            k = 0
            num[i] = 0
        i += 1
        r = i
        if i == len(num):
            i = 0
    print(num)
    print(max(num))
