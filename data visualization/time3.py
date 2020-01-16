import pandas as pd
import numpy as np

t = pd.date_range(start='2018/8/1 12:13:30', periods=5, freq='10H', normalize=True, tz='Asia/Hong_Kong')
print(t)

"""
dateIndex = pd.date_range('2018-1-1', periods=50, freq='W-FRI')

print(dateIndex)
"""