# 题目：对10个数进行排序。


if __name__ == "__main__":
    l = [9, 2, 1, 3, 5, 4, 8, 6, 7]
    for i in range(len(l) - 1):
        min = i
        for j in range(i + 1, len(l)):
            if l[min] > l[j]: min = j
        l[i], l[min] = l[min], l[i]
    print('排列之后：', l)
