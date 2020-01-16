import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


# 这个可以让全部显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
plt.rcParams['font.size'] = 7.5  # 条件显示图像的行列字体大小
plt.rcParams['axes.unicode_minus'] = False  # 显示负号


# 导入数据
f1 = open('data1.csv')
data1 = pd.read_csv(f1)
f1.close()

f2 = open('data2.csv')
data2 = pd.read_csv(f2)
f2.close()
print('*******************************************************')


# 缺失值 & 空值
print(data1.isnull().sum())
print(data2.isnull().sum())
print('*******************************************************')


# 重复值
print(data1.duplicated().sum())
print(data2.duplicated().sum())
print('*******************************************************')


# 最大值 、最小值、标准差、 25%、 50%、75%、平均值
print(data1.describe())
print(data2.describe())
print('*******************************************************')


# 变成时间标签
index_1 = pd.to_datetime(data1['时间'].values.tolist())
data1.index = index_1
print(data1.head())
print('--------------------------------------------------------')

index_2 = pd.to_datetime(data2['时间'].values.tolist())
data2.index = index_2
print(data2.head())
print('*******************************************************')


# 合并
merge = pd.merge(data1, data2, on='时间')
print(merge.head())
print('*******************************************************')


# 第一大题的第五小题
for i in data2.columns.tolist():

    x = i + '_x'
    y = i + '_y'

    plt.figure()
    try:
        merge[x].plot(linestyle='--')
        merge[y].plot()
        # plt.plot(merge[x], linestyle='--')
        # plt.plot(merge[y])
    except:
        break

    plt.legend()
    plt.show()


# 直方图 & 核密度
for i in data2.columns.tolist():
    if i == '时间':
        continue

    plt.figure()
    plt.title(i, fontsize=15)
    try:
        sns.distplot(data1[i], bins=10, color='r', kde=True, kde_kws={'color': 'r'}, label='data1')
    except:
        pass
    sns.distplot(data2[i], bins=10, color='b', kde=True, kde_kws={'color': 'b'}, label='data2')
    plt.legend()
    # plt.savefig('直方图与核密度图/' + i + '.jpg')
    plt.show()


# 折线图
# 当 n 为 False 时为均值折线图
n = False
for i in data2.columns.tolist():
    if i == '时间':
        continue
    fig = plt.figure()
    fig.tight_layout()
    plt.title(i)
    if n:
        try:
            plt.plot(data1[i], label='data1', linestyle='--')
        except:
            pass

        plt.plot(data2[i], label='data2')

    else:
        try:
            plt.plot(data1[i].resample('W-MON').mean(), linestyle='--', label='data1')

        except:
            pass

        plt.plot(data2[i].resample('W-MON').mean(), label='data2')

    plt.legend()
    # plt.savefig('均值折线图/' + i + '.jpg')
    plt.show()


# 散点图
for j in data2.columns.tolist():
    if j == '时间':
        continue

    for i in data2.columns.tolist():
        if i == '时间':
            continue
        fig = plt.figure()
        fig.tight_layout()
        plt.xlabel(j, fontsize=15)  # fontsize=15设置字体大小
        plt.ylabel(i, fontsize=15)
        try:
            plt.scatter(data1[j], data1[i], label='data1', s=100)
        except:
            pass
        plt.scatter(data2[j], data2[i], label='data2', s=50, marker='p')
        plt.legend()
        # plt.savefig('散点图/' + j + '--' + i + '.jpg')
        plt.show()


# 盒状图
nn = 1
if nn == 1:
    fig = plt.figure()
    fig.tight_layout()

    plt.subplot(1, 2, 1)
    plt.title('data1')
    data1.boxplot(notch=True)


    plt.subplot(1, 2, 2)
    plt.title('data2')
    data2.boxplot(notch=False)

    # plt.savefig('盒状图/data1-data2.jpg')
    plt.show()







