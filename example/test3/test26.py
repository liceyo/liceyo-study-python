# 题目：利用递归方法求5!。


def factorial(x):
    if x > 1:
        return x * factorial(x - 1)
    return 1


print(factorial(5))
print(factorial(10))
