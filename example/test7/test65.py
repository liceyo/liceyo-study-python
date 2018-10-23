# 画折线图

import matplotlib.pyplot as plt

if __name__ == '__main__':
    font = {'family': 'FangSong',
            'size': '12'}
    plt.rc('font', **font)        # 步骤一（设置字体的更多属性）
    plt.rc('axes', unicode_minus=False)  # 步骤二（解决坐标轴负数的负号显示问题）
    x = [20, 50, 100, 150, 200, 300, 400, 600, 1000]
    y1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    plt.figure(figsize=(8, 4.9))
    plt.plot(x, y1, label=u"测试1", color='r', marker="o", linewidth=1)
#     plt.plot(x, [i**2 for i in y1], label=u"测试2",
#              color='b', marker="o", linewidth=1)
#     plt.plot(x, [i*2 for i in y1], label=u"测试3",
#              color='g', marker="o", linewidth=1)
    for a, b in zip(x, y1):
        plt.text(a, b, (a, b), ha='center', va='bottom', fontsize=10)
    plt.xlabel("数量")
    plt.ylabel("时间")
    plt.title("测试")
    plt.grid(linestyle=':')
    plt.legend()
    plt.show()
