# 题目：编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n

if __name__ == '__main__':
    n = int(input('input a number:\n'))
    s = 0.0
    if n % 2 == 0:
        s = sum([1.0/i for i in range(2, n+1, 2)])
    else:
        s = sum([1.0/i for i in range(1, n+1, 2)])
    print(s)
