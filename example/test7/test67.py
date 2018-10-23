# 画饼图

import numpy as np
import matplotlib.pyplot as plt

font = {'family': 'FangSong',
        'size': '12'}
plt.rc('font', **font)        # 步骤一（设置字体的更多属性）
plt.rc('axes', unicode_minus=False)  # 步骤二（解决坐标轴负数的负号显示问题）
labels = '一季度', '二季度', '三季度', '四季度'
fracs = [15, 30.55, 44.44, 10]
explode = [0, 0.1, 0, 0]  # 0.1 凸出这部分，
plt.axes(aspect=1)
plt.pie(x=fracs, labels=labels, explode=explode, autopct='%3.1f %%',
        shadow=True, labeldistance=1.1, startangle=90, pctdistance=0.6)
plt.title("测试")
plt.show()
