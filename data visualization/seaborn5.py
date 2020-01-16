import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 绘制核密度图
iris = sns.load_dataset("iris")
g = sns.jointplot("sepal_width", "petal_length", data=iris,
                    kind="kde", space=0, color="g")
plt.show(g)