import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
#  单变量分布
sns.set()
np.random.seed(0)
arr = np.random.randn(1000)
print(arr)
ax = sns.distplot(arr, bins=100, kde=True, kde_kws={'color': 'r'}, rug=True, rug_kws={'color': 'g'})  #  绘制直方图
plt.show(ax)