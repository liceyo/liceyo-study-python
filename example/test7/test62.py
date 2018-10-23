# 题目：坐标轴设置，并绘制散点图

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

font = {'family': 'FangSong',
        'size': '12'}
plt.rc('font', **font)        # 步骤一（设置字体的更多属性）
plt.rc('axes', unicode_minus=False)  # 步骤二（解决坐标轴负数的负号显示问题）

x1 = [1.2, 2.4, 3.1, 4.6]
y1 = [1, 2, 3, 4]

x2 = [1, 2, 3, 4]
y2 = [1.2, 2.4, 3.1, 4.6]

n = 10
x3 = np.random.randint(1, 10, n)
y3 = np.random.randint(1, 10, n)

plt.scatter(x1, y1, marker='x', color='red', s=10, label='First')
plt.scatter(x2, y2, marker='1', color='blue', s=10, label='Second')
plt.scatter(x3, y3, marker='o', color='green', s=10, label='Third')
plt.legend(loc='best')

plt.xlabel('X轴')
plt.ylabel('Y轴')  # 设置坐标轴标签
plt.xlim(0, 10)
plt.ylim(0, 13)

ax = plt.gca()
# 修改主刻度
xmajorLocator = MultipleLocator(1)  # 将x主刻度标签设置为1的倍数
xmajorFormatter = FormatStrFormatter('%1.2f')  # 设置x轴标签文本的格式
ymajorLocator = MultipleLocator(1)  # 将y轴主刻度标签设置为1的倍数
ymajorFormatter = FormatStrFormatter('%1.2f')  # 设置y轴标签文本的格式
# 设置主刻度标签的位置,标签文本的格式
ax.xaxis.set_major_locator(xmajorLocator)
ax.xaxis.set_major_formatter(xmajorFormatter)
ax.yaxis.set_major_locator(ymajorLocator)
ax.yaxis.set_major_formatter(ymajorFormatter)
# 修改次刻度
xminorLocator = MultipleLocator(0.5)  # 将x轴次刻度标签设置为0.2的倍数
yminorLocator = MultipleLocator(0.5)  # 将此y轴次刻度标签设置为0.2的倍数
# 设置次刻度标签的位置,没有标签文本格式
ax.xaxis.set_minor_locator(xminorLocator)
ax.yaxis.set_minor_locator(yminorLocator)
# 设置 上、右 两条边框不显示
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
# 将下、左 两条边框分别设置为 x y 轴
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
# 将两条坐标轴的交点进行绑定
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))
plt.legend()
# 网格使用虚线，使用此刻度
plt.grid(linestyle=':', which='minor')
plt.show()
