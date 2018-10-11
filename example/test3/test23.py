# 题目：打印出菱形图案

cnt = 4
for i in range(0, 2 * cnt + 1):
    if i < cnt:
        for x in range(cnt - i):
            print(' ', end='')
        for x in range(2 * i + 1):
            print('*', end='')
    else:
        y = 2 * cnt - i
        for x in range(cnt - y):
            print(' ', end='')
        for x in range(2 * y + 1):
            print('*', end='')
    print()
