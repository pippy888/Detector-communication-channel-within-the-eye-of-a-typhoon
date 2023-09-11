# import matplotlib.pyplot as plt
#
# # 创建一个 Figure 对象和两个坐标轴对象
# fig, ax1 = plt.subplots()
# ax2 = ax1.twinx()  # 创建一个与 ax1 共享 x 轴的新坐标轴
#
# # 绘制 x 轴数据
# x = [1, 2, 3, 4, 5]
# y1 = [10, 20, 30, 40, 50]
# ax1.plot(x, y1, 'b-')  # 在第一个坐标轴上绘制蓝色曲线
#
# # 绘制 y 轴数据
# y2 = [100, 200, 300, 400, 500]
# ax2.plot(x, y2, 'r-')  # 在第二个坐标轴上绘制红色曲线
#
# # 设置第一个坐标轴的属性
# ax1.set_xlabel('X')
# ax1.set_ylabel('Y1', color='b')
# ax1.tick_params('y', colors='b')

# import matplotlib.pyplot as plt
#
# x = list(range(1, 13, 2))  # x 轴刻度点
# y = [25, 26, 24, 28, 30, 29]  # y 轴温度数据
#
# plt.plot(x, y, 'b-')  # 绘制折线图，蓝色线条
#
# plt.xlabel('Month')  # 设置 x 轴标签
# plt.ylabel('Temperature')  # 设置 y 轴标签
#
# plt.show()  # 显示图形
#
# # 设置第二个坐标轴的属性
# ax2.set_ylabel('Y2', color='r')
# ax2.tick_params('y', colors='r')
#
# plt.show()

# import numpy as np
#
# print(np.logspace(start=0 ,stop= 63,num=64 , base=2,dtype='uint64'))

# import numpy as np
# import matplotlib.pyplot as plt
#
# x = np.arange(100)
#
# # 创建图像布局对象fig
# fig = plt.figure(figsize = (12, 6))
#
# # 221代表创建2行2列一共4个子图，并从左往右第1个子图开始绘图。
# ax1 = fig.add_subplot(221)
# ax1.plot(x, x)
#
# ax2 = fig.add_subplot(222)
# ax2.plot(x, -x)
#
# ax3 = fig.add_subplot(223)
# ax3.plot(x, x ** 2)
#
# ax4 = fig.add_subplot(224)
# ax4.plot(-x, x ** 2)
#
# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
#
# # 将画布分割为2行2列，起始值为0。
# fig, axes = plt.subplots(figsize = (12, 6), nrows = 2, ncols = 2)
# # 给第1行第1列绘图
# axes[0][0].hist(np.random.rand(500), label = 'hist0', edgecolor = 'black')
# # 给图形添加标签
# axes[0][0].legend()
#
# axes[0][1].hist(np.random.rand(500), label = 'hist1', edgecolor = 'black')
# axes[0][1].legend()
#
# axes[1][0].hist(np.random.rand(500), label = 'hist2', edgecolor = 'black')
# axes[1][0].legend()
#
# axes[1][1].hist(np.random.rand(500), label = 'hist3', edgecolor = 'black')
# axes[1][1].legend()
#
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
# if __name__ == '__main__':
#     x = np.linspace(-np.pi, np.pi, 256)
#     y1 = np.sin(x)
#     y2 = np.cos(x)
#
#     fig1 = plt.figure(num='first')
#     fig1.suptitle('first figure')
#     plt.plot(x, y1)
#
#     fig2 = plt.figure(num='second')
#     fig2.suptitle('second figure')
#     plt.plot(x, y2)
#
#     plt.figure(num=1)  # plt.figure(num='first')
#     plt.plot(x, y2)
#     plt.show()

import math
print((math.sin(math.degrees(5)))**1.2)