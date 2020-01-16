
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#  不知为何，这几个图不能同时显示
tips = sns.load_dataset("tips")

# 分组的散点图
#ax = sns.stripplot(x="day", y="total_bill", data=tips)

# 添加抖动项的散点图，jitter可以是0.1,0.2...这样的小数，表示抖动的程度大小
#ax = sns.stripplot(x="day", y="total_bill", data=tips, jitter=True)

# 是不是想横着放呢，很简单的，x-y顺序换一下就好了
ax = sns.stripplot(x="total_bill", y="day", data=tips, jitter=True)


plt.show(ax)






