import pandas as pd
import numpy as np

dateTimeIdex = pd.to_datetime(['20191201', '20191102', '20181203'])

print(dateTimeIdex)

s1 = pd.Series(data=[1, 2, 3], index=dateTimeIdex)

print(s1)
print(s1[1])
print(s1['2019-12'])