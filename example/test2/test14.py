# 题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。


def reduce_num(n):
    print('{} = '.format(n), end='')
    if not isinstance(n, int) or n <= 0:
        print('请输入一个正确的数字 !')
        exit(0)
    elif n == 1:
        print('{}'.format(n), end='')
    while n != 1:  # 循环保证递归
        for index in range(2, n + 1):
            if n % index == 0:
                n = int(n / index)  # n 等于 n/index
                if n == 1:
                    print(index)
                else:  # index 一定是素数
                    print('{} * '.format(index), end='')
                break


reduce_num(90)
reduce_num(100)
reduce_num(101)
reduce_num(102)
reduce_num(111)
