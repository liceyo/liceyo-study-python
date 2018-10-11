# 题目：斐波那契数列。

def fib1(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibs = [1, 1]
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs


# 使用递归
def fib2(n):
    if n == 1 or n == 2:
        return 1
    return fib2(n - 1) + fib2(n - 2)


# 使用循环
def fib3(n):
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    return a


print(fib1(int(input("num:"))))
