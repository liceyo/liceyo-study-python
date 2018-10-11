# coding=utf-8
# 排序


# 冒泡排序
def bubble_sort(array):
    for i in range(0, len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


# 快速排序
def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        left = [i for i in array[1:] if i <= array[0]]
        right = [i for i in array[1:] if i > array[0]]
        return quick_sort(left) + [array[0]] + quick_sort(right)


# 插入排序
def insert_sort(array):
    for i in range(1, len(array)):
        x = array[i]
        j = i
        for j in range(i, -1, -1):
            if x < array[j - 1]:
                array[j] = array[j - 1]
            else:
                break
        array[j] = x


a = [7, 2, 5, 1, 3, 9, 6, 4, 8]
bubble_sort(a)
print(a)

a = [7, 2, 5, 1, 3, 9, 6, 4, 8]
a = quick_sort(a)
print(a)

a = [7, 2, 5, 1, 3, 9, 6, 4, 8]
insert_sort(a)
print(a)
