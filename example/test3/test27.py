# 题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。


def r_output(s, l):
    if l > 0:
        print(s[l - 1])
        r_output(s, l - 1)


s = input("Input:")
r_output(s,len(s))