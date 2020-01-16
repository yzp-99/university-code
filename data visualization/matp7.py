# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 8))
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = True
#  柱形图1
plt.subplot(221)
plt.title('2001年第一季度国民生产总值直方图')

name_list = ['第一产业', '第二产业', '第三产业']
num_list = [2000, 9000, 9800]
x = list(range(len(num_list)))
total_width, n = 0.8, 2
width = total_width / n
plt.bar(x, num_list, width=width, tick_label=name_list, fc='g')

# 2
plt.subplot(222)
plt.title('2017年第一季度国民生产总值直方图')

name_list1 = ['第一产业', '第二产业', '第三产业']
num_list1 = [10000, 75000, 110000]
x = list(range(len(num_list1)))
total_width, n = 0.8, 2
width = total_width / n
plt.bar(x, num_list1, width=width, tick_label=name_list1, fc='b')

# 3
plt.subplot(223)
plt.title('2001年第一季度国民生产总值行业构成直方图')

name_list2 = ['农业', '工业', '建筑', '批发', '交通', '餐饮', '金融','房地产','其它']
num_list2 = [2000, 9000, 1100, 2100, 1600, 800, 1500, 1200, 3400]
x = list(range(len(num_list2)))
total_width, n = 0.8, 2
width = total_width / n
plt.bar(x, num_list2, width=width, tick_label=name_list2, fc='y')

# 4
plt.subplot(224)
plt.title('2017年第一季度国民生产总值行业构成直方图')

name_list3 = ['农业', '工业', '建筑', '批发', '交通', '餐饮', '金融', '房地产', '其它']
num_list3 = [9000, 61000, 9800, 17000, 8600, 3600, 16000, 12000, 43000]
x = list(range(len(num_list3)))
total_width, n = 0.8, 2
width = total_width / n
plt.bar(x, num_list3, width=width, tick_label=name_list3, fc='r')





plt.legend()
plt.show()