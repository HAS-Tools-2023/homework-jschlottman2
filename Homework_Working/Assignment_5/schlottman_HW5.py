# schlottman_HW5 Numpy Pt.2

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week5.txt'
filepath = os.path.join('../../data', filename)
print(os.getcwd())
print(filepath)

# %%
# DON'T change this part -- this creates the lists you 
# should use for the rest of the assignment
# no need to worry about how this is being done now we will cover
# this in later sections. 

#Read the data into a pandas dataframe
data=pd.read_table(filepath, sep = '\t', skiprows=30,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code']
        )

# Expand the dates to year month day
data[["year", "month", "day"]] =data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)

# Make a numpy array of this data
flow_data = data[['year', 'month','day', 'flow']].to_numpy()

# Getting rid of the pandas dataframe since we wont be using it this week
del(data)

# %%

# Make a new numpy array including only data from period 1/1/2015-12/31/2019
flow_5yr = flow_data[(flow_data[:,0] >= 2015) & (flow_data[:,0] <= 2019),:]
print(flow_5yr)

# %%
#calcuate average flow value of 5 year period.
flow_average = np.mean(flow_5yr)
print(flow_average)

# %%
# print dimensions
print(np.size(flow_5yr))
print(np.ndim(flow_5yr))
# %%
# Convert daily average flow from cfs to cubic feet
flow_convert=flow_average**86400
print(flow_convert)

# %%
# convert daily average flow from cfs to cubic feet with for loop
flow_5yr[:,3]*86400
flow_daily=[]
for i in range(len(flow_5yr[:,1])):
    temp=flow_5yr[i,3]*86400
    flow_daily=np.append(flow,temp)
print(flow_daily)  

# %%
# Create a time series of monthly average flow:
flow_monthly=np.zeros((60,3))
flow_monthly[:,0]=np.tile(np.arange(2015,2020,1),12)
flow_monthly[:,1]=np.tile(np.arange(1,13,1),5)
print(flow_monthly)

# %%
