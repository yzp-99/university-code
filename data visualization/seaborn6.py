import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# 普通的散点图
ax1 = sns.stripplot(x=tips["total_bill"])
# 带分布密度的散点图
#ax2 = sns.swarmplot(x=tips["total_bill"])

plt.show(ax1)
#plt.show(ax2)
