# 题目：打印出杨辉三角形

if __name__ == '__main__':
    arr = []
    # 创建三角形数组
    for i in range(10):
        arr.append([])
        for j in range(i+1):
            arr[i].append(1)
    for i in range(2, 10):
        for j in range(1, i):
            arr[i][j] = arr[i - 1][j-1] + arr[i - 1][j]
    for i in range(10):
        for j in range(i + 1):
            print(arr[i][j],end=' ')
        print()
