"""题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，
小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？"""

a = 1
b = 1
c = 0
for i in range(1, int(input("month:")) + 1):
    if i >= 3:
        # 先运算后赋值
        a, b = b, a + b
    if b > 100000000 and c == 0:
        c = i
    print("%4ld - %d" % (i, b))
print(c)
