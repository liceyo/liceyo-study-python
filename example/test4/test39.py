# 题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。

a = [1, 4, 6, 9, 13, 16, 19, 28, 40, 100]
x = int(input("x="))
l = len(a)
if x >= a[l - 1]:
    a.append(x)
else:
    b = []
    j = True
    for i in a:
        if i > x and j:
            b.append(x)
            j = False
        b.append(i)
    a = b
print(a)
