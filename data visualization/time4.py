import pandas as pd
from pandas.tseries import offsets
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns


#  1
time_off = offsets.DateOffset(months=5, days=10, hours=5, minutes=6, seconds=52)
time_range = pd.date_range('2010-01-01', '2019-12-10', freq=time_off)
print(time_range)



#  2

np.random.seed(0)
gold = np.random.randn(len(time_range)) + 300

np.random.seed(1)
diamond = np.random.randn(len(time_range)) + 700

np.random.seed(2)
house = np.random.randn(len(time_range)) + 2500

data = {'黄金价格 (Gold， 400-500)': gold,
        '钻石价格（Diamond： 600-800）': diamond,
        '房子价格（House：2000-3000）': house}

data = pd.DataFrame(data=data, index=time_range)
print(data)

plt.figure(figsize=(9, 6))


# 3
# 显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.size'] = 7.5  # 条件显示图像的行列字体大小
plt.rcParams['axes.unicode_minus'] = False  # 显示负号


plt.subplot(1, 3, 1)
plt.xticks(rotation=45)
plt.title('房子')
plt.plot(data['房子价格（House：2000-3000）'])

plt.subplot(1, 3, 2)
plt.xticks(rotation=45)
plt.title('黄金')
plt.plot(data['黄金价格 (Gold， 400-500)'])

plt.subplot(1, 3, 3)
plt.xticks(rotation=45)
plt.title('钻石')
plt.plot(data['钻石价格（Diamond： 600-800）'])



# 4

plt.subplot(1, 2, 1)
plt.xticks(rotation=45)
plt.title('房子与黄金')
plt.scatter(data['房子价格（House：2000-3000）'], data['黄金价格 (Gold， 400-500)'])

plt.subplot(1, 2, 2)
plt.xticks(rotation=45)
plt.title('房子与钻石')
plt.scatter(data['房子价格（House：2000-3000）'], data['钻石价格（Diamond： 600-800）'])



#  5

t_time = []
t1 = []
t2 = []
t3 = []
for i in range(2010, 2020):
    new_data = data[str(i)]

    describe_data = new_data.describe()

    t_time.append(i)
    t1.append(describe_data.loc['mean', '房子价格（House：2000-3000）'])
    t2.append(describe_data.loc['mean', '黄金价格 (Gold， 400-500)'])
    t3.append(describe_data.loc['mean', '钻石价格（Diamond： 600-800）'])

plt.subplot(1, 3, 1)
plt.xticks(rotation=45)
plt.title('房子年度平均值')
plt.plot(t_time, t1)

plt.subplot(1, 3, 2)
plt.xticks(rotation=45)
plt.title('黄金年度平均值')
plt.plot(t_time, t2)

plt.subplot(1, 3, 3)
plt.xticks(rotation=45)
plt.title('钻石年度平均值')
plt.plot(t_time, t3)

plt.show()
