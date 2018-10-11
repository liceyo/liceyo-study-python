# 题目：输入三个整数x,y,z，请把这三个数由小到大输出。

arr = []
for i in range(0, 3):
    j = int(input("INT:\n"))
    arr.append(j)
arr.sort()
print(arr)
