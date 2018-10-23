import matplotlib.pyplot as plt

if __name__ == '__main__':
    font = {'family': 'FangSong',
            'size': '12'}
    plt.rc('font', **font)        # 步骤一（设置字体的更多属性）
    plt.rc('axes', unicode_minus=False)  # 步骤二（解决坐标轴负数的负号显示问题）
    num_list = [1.5, 0.6, 7.8, 6]
    name_list = ['星期一', '星期二', '星期三', '星期四']
    # 一般展示
    # plt.bar(range(len(num_list)), num_list, color='rggb', tick_label=name_list)
    # 堆叠展示
    plt.bar(range(len(num_list)), num_list, label='男', fc='g')
    num_list1 = [1, 2, 3, 1]
    plt.bar(range(len(num_list)), num_list1, bottom=num_list,
            label='女', tick_label=name_list, fc='r')
    plt.xlabel("数量")
    plt.ylabel("时间")
    plt.title("测试")
    plt.grid(axis='y', linestyle=':')
    plt.legend()
    plt.show()
