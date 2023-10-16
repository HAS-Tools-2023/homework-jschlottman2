# Python file for HW6 Pandas Dataframes

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# Set the file name and path to where you have stored the data
filename = 'streamflow_week6.txt'
#filepath = os.path.join('../../data', filename)
filepath = os.path.join('./', filename)
print(os.getcwd())
print(filepath)

#filepath = '../Assignments/Solutions/data/streamflow_week6.txt'

# %%
#Read the data into a pandas dataframe
data=pd.read_table(filepath, sep = '\t', skiprows=30,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code']
        )

# Expand the dates to year month day
data[["year", "month", "day"]] =data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)

# %%
# Data types
print(data)
print(data.index)
print(data.info())
print(data.describe())

# %%
#Calculations of flow column
data.min()
data.mean()
data.max()
data.std()
data.quantile()
# %%

