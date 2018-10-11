# 题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。

x = input("请输入一个数:\n")

if x.isalnum() and int(x) > 0 and len(x) <= 5:
    print("Length:", len(x))
    for i in range(len(x)):
        print(x[len(x) - i - 1])
else:
    print("ERROR")
