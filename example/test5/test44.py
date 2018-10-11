# 两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵：

X = [
    [12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]
]

Y = [
    [5, 8, 1],
    [6, 7, 3],
    [4, 5, 9]
]

Z = []

for i in range(3):
    u = []
    for j in range(3):
        u.append(X[i][j] + Y[i][j])
    Z.append(u)
print(Z)
