"""
题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；
再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
"""

h = 100.0
l = 0.0
for i in range(1, 20):
    if i == 1:
        l = h
    else:
        l += h * 2
    h /= 2
    print("i=%2ld,length=%13lf ,high=%10lf" % (i, l, h))

tour = []
height = []