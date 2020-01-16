import numpy as np
import pandas as pd

da = pd.DataFrame([1, 23, 5, 4, 6, 77], columns=[1], index=[["1", "1","1",
                                                      "2", "2",
                                                      "3"],
                                                     [1, 2, 3,
                                                      1, 2,
                                                      5]])

# print(da)

from pandas import MultiIndex
# 创建包含多个元组的列表
list_tuples = [('A', 'A1'), ('A', 'A2'), ('B', 'B1'),
               ('B', 'B2'), ('B', 'B3')]
# 根据元组列表创建一个MultiIndex对象
# print(pd.DataFrame([1,2,3,4,5],index=list_tuples))

multi_index = MultiIndex.from_tuples(tuples=list_tuples,
                                     names=['1', '2'])
# print(multi_index)
# print(da.index)

da_new = pd.DataFrame([1, 2, 3, 4, 5], index=multi_index)
# print(da_new)

# print(da_new[0])
# print(da_new.loc["A"])
# print(da_new.iloc[1,0])


dd = pd.Series([1, 2, 3, 4, 5, 6], index=[[1,1,2,2,3,4],[11,22,33,44,55,666]],name="we12")
print(dd)
# 只有用 pd.Series 才可以用下面的方法
# print(dd[1])
# print(dd[:,33])
# print(type(dd[:,33]))
# print(dd[:,33][2]) # 这里的 2 是因为你 dd[:,33] 的行标签是 2
# print(dd.set_value(1,3)) # 修改(第一个参数是需要修改的行标签，第二个是修改后的值)(如果行标签不存在，则默认添加一行)
# print(dd.swaplevel())


df = pd.Series([111],index=[[1],[66]])
f1 = dd.append(df).sort_index() # 一个简单的添加（在外层索引 1 中，添加其内层索引以及对应的值）
print(f1)

df = pd.Series([0],index=[[1],[68]])
f2 = dd.append(df).sort_values() # 添加不会让原来的数据的进行改变
# f2 = f1.append(df).sort_values()
print(f2) # Series 用 append 来添加数据（目前只会这种方法，不知道还有其他的吗）
# Series 如果想插入，可以先切片（分成多分），再添加新数据，在合并
