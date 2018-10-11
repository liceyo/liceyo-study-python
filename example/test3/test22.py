"""
题目：两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。
已抽签决定比赛名单。有人向队员打听比赛的名单。
a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。
"""
a = ['y', 'z']
b = ['x', 'y', 'z']
c = ['y']
e = {'c': c, 'a': a, 'b': b}
# e_sort = sorted(e.items(), key=lambda x: len(x[1]))
r = []
for i, j in e.items():
    while len(e[i]) != 1:
        for k in r:
            if k in e[i]:
                e[i].remove(k)
    if len(e[i]) == 1:
        r.append(e[i][0])
print(e)
