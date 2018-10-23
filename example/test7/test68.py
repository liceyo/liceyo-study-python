# 多子图

import matplotlib.pyplot as plt
import math
import numpy as np
from matplotlib.ticker import MultipleLocator, FormatStrFormatter


x = np.arange(-math.pi, math.pi, 0.01)
y = [np.sin(xx) for xx in x]

xmajorLocator = MultipleLocator(1)  # 将x主刻度标签设置为1的倍数
xmajorFormatter = FormatStrFormatter('%1.2f')  # 设置x轴标签文本的格式
ymajorLocator = MultipleLocator(1)  # 将y轴主刻度标签设置为1的倍数
ymajorFormatter = FormatStrFormatter('%1.2f')  # 设置y轴标签文本的格式
xminorLocator = MultipleLocator(0.5)  # 将x轴次刻度标签设置为0.2的倍数
yminorLocator = MultipleLocator(0.5)  # 将此y轴次刻度标签设置为0.2的倍数


def create_ax(fig, subplot):
    ax = fig.add_subplot(subplot)
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['left'].set_position(('data', 0))
    # 设置主刻度标签的位置,标签文本的格式
    ax.xaxis.set_major_locator(xmajorLocator)
    ax.xaxis.set_major_formatter(xmajorFormatter)
    ax.yaxis.set_major_locator(ymajorLocator)
    ax.yaxis.set_major_formatter(ymajorFormatter)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    ax.grid(linestyle=':', which='minor')
    return ax


fig = plt.figure(figsize=(6, 6))
# plt.subplot(111)和plt.subplot(1,1,1)是等价的。意思是将区域分成1行1列，当前画的是第一个图（排序由行至列）
ax1 = create_ax(fig, 231)
ax2 = create_ax(fig, 232)
ax3 = create_ax(fig, 233)
ax4 = create_ax(fig, 234)
ax5 = create_ax(fig, 235)
ax6 = create_ax(fig, 236)
ax1.plot(x, y, color='r', linestyle='-')
ax2.plot(x, y, color='g', linestyle='-.')
ax3.plot(x, y, color='b', linestyle='--')
ax4.plot(x, y, color='c', linestyle=':')
ax5.plot(x, y, color='m', linestyle='-.')
ax6.plot(x, y, color='y', linestyle='-.')

plt.show()
