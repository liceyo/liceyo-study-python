# 题目：画椭圆。

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse

delta = 10.0  # degrees

angles = np.arange(0, 360 + delta, delta)
print(angles)
# Ellipse 参数解释：(0,0) 中心点，4是两点最长距离，2是两点最短距离，a是长轴与x轴正向的角度
ells = [Ellipse((0, 0), 30, 8, a) for a in angles]

a = plt.subplot(111, aspect='equal')

for e in ells:
    e.set_clip_box(a.bbox)
    e.set_alpha(0.1)
    a.add_artist(e)

plt.xlim(-20, 20)
plt.ylim(-20, 20)

plt.show()
