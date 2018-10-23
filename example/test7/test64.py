# 题目：画矩形

import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

for i in range(5):
    rect = plt.Rectangle((i,0),5,3)
    ax.add_patch(rect)

plt.xlim(-5, 10)
plt.ylim(-5, 10)
plt.show()
