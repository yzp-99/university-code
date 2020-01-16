import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 双变量分布

# 通过kind参数，除了绘制散点图，还要绘制拟合的直线，拟合的核密度图
tips = sns.load_dataset("tips")

g = sns.jointplot("total_bill", "tip", data=tips, kind="reg")
# 使用六角形代替点图图
g1 = sns.jointplot("total_bill", "tip", data=tips, kind="hex")

g2 = sns.jointplot("total_bill", "tip", data=tips, kind="kde")

# 控制图形的大小和颜色
g3 = sns.jointplot("total_bill", "tip", data=tips, size=5, ratio=3, color="g")

plt.show(g)
plt.show(g1)
plt.show(g2)
plt.show(g3)
















