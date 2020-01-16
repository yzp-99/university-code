
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")




# 重点来了，分组绘制，而且是分组后分开绘制，在柱状图中，跟分组柱状图类似的。
# 通过 hue, dodge 参数控制
# 1.分组
ax = sns.stripplot(x="size", y="total_bill", hue="sex", data=tips, jitter=True)
# 2.分开绘制
#ax = sns.stripplot(x="day", y="total_bill", hue="smoker", data=tips, jitter=True, palette="Set2", dodge=True)


plt.show(ax)