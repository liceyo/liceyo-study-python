# 题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。


x = input("请输入一个数:\n")

if x.isalnum() and int(x) > 0 and len(x) <= 5:
    print("是否是回文数：", x[0] == x[4] and x[1] == x[3])
else:
    print("ERROR")
