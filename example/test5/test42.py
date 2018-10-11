# 题目：学习使用auto定义变量的用法。啥玩意？

num = 2


def auto_func():
    num = 1
    print('internal block num = %d' % num)
    num += 1


for i in range(3):
    print('The num = %d' % num)
    num += 1
    auto_func()
