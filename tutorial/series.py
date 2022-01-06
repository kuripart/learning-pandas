import pandas as pd
import numpy as np

# DeprecationWarning: The default dtype for empty Series will be 'object' instead of 'float64' in a future version. Specify a dtype explicitly to silence this warning.
s = pd.Series(dtype='string')
print(s)

# Series([], dtype: string)

data = np.array(['a', 'b', 'c', 'd'])
s = pd.Series(data, dtype='string', index=[2,3,1,9])
print(s)

# 2    a       
# 3    b       
# 1    c       
# 9    d       
# dtype: string

print(s[2])
print(s[3])
print(s[1])
print(s[9])

s = pd.Series(data, index=[1,2,3,4])
print(s[1])
print(s[2])
print(s[3])
print(s[4])

s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])

#retrieve the first element
print(s)
print(s[0])
print(s['e'])
print(s[['e', 'a', 'c']])


data = {'a' : 0., 'b' : 1., 'c' : 2.}
print(pd.Series(data))
print(pd.Series(data, ['a', 'd', 'c', 'e']))
print(pd.Series(5, index=[0, 1, 2, 3]))
print(pd.Series(5, index=[0, 1, 2, 3])[:3]) # 1st 3
print(pd.Series(5, index=[0, 1, 2, 3])[-3:]) # last 3
try:
    print(s['x'])
except KeyError as e:
    print(f"{e} not found")