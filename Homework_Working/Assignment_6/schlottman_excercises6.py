# %%
import numpy as np
import pandas as pd

# %%
data = np.ones((7,3))
data_frame = pd.DataFrame(data,
                          columns=['data1', 'data2', 'data3'],
                          index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])
# %%
data_frame.loc[['a','e']] = 3
print(data_frame)
# %%
print(data_frame.loc[['a','b','c','d']]*7)
# %%
data = np.ones((7,3))
data_frame = pd.DataFrame(data,
                          columns=['data1', 'data2', 'data3'],
                          index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])
print(data_frame.loc[['a','c','e','g'], ['data1', 'data3']]=0)
print(data_frame.loc[['b','d','f']])
# %%
print(data_frame.iloc[[0,]])