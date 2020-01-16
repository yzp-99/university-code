import matplotlib.pyplot as plt
import numpy as np



plt.figure(figsize=(6, 6),dpi=150)

x = np.arange(0, 110, 10)  # 产生10个数，0-110之间，间隔为10
#y = np.arange(0, 110, 10)
plt.subplot(121)
#  支持中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


plt.title('折线图')  # 图的名称


plt.xlabel("年份")  # x轴的名称
plt.xlim((0, 100))  # x轴的数据范围
plt.xticks([0, 25, 50, 75, 100], ['0%', '25%', '50%', '75%', '100%'])  # x轴的刻度名称

plt.ylabel("生产总值（亿元）")
plt.ylim((0, 100))
plt.yticks([0, 25, 50, 75, 100], ['0%', '25%', '50%', '75%', '100%'])

plt.plot(x, x*2)
plt.plot(x, x**2)  # 画另一个图案：折线图
#plt.plot(y, y)
#plt.plot(y, y*2)

plt.subplot(122)
plt.legend(['y=x', 'y=x*2'])
#plt.savefig("matp2.png")
plt.show()