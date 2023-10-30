# Assignment: Week 8 Forecast Script
# Author Name: Jason Schlottman
# Name of user: 
# Date: 10/23/2023
# Explanation: Run a few cells & generate forecast estimates.
# Click the 'run-cell' button and execute each of the following steps to complete the script.

# %%
# Import modules
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime

# %%
filename = 'streamflow_week8.txt'
# Read in our data as a dataframe
data = pd.read_table(filename, sep='\t', skiprows=30,
                     names=['agency_cd', 'site_no',
                            'datetime', 'flow', 'code'],
                     )

# %%
# DataFrame, making the dates into a datetime object
data2 = pd.read_table(filename, sep='\t', skiprows=30,
                      names =['agency_cd', 'site_no',
                              'datetime', 'flow', 'code'],
                              parse_dates =['datetime']
                      )

# %%
#Expand dates to day,month,year
data[["year", "month", "day"]] =data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)

# %%
#make lists of the data
flow = data.flow.values.tolist()
date = data.datetime.values.tolist()
year = data.year.values.tolist()
month = data.month.values.tolist()
day = data.day.values.tolist()

# %%
# Create Graphs relating to flow data

# Histogram:
Z=np.random.normal(0, 1, 100)
plt.xlabel('Datetime')
plt.ylabel('Flow Observations')
plt.title('Flow Distribution Histogram')
plt.hist(Z)

# Scatter Plot 
df=pd.DataFrame(data2)
df.plot.scatter(x='datetime', y='flow', color='green')
plt.xlabel("Time")
plt.ylabel('Flow')
plt.title('Observed Flow Over Time')

# %%
#Identify flow values in October of previous years less than 90 cfs to relate to average historical observed values.
flowlist=[]
for i in range(len(flow)):
    if flow[i]<90 and month[i] ==10:
        flowlist.append(i)
q=len(flowlist)

for i in range(len(flow)):
    if flow[i]<91 and month[i] ==10:
        flowlist.append(i)
q2=len(flowlist)

# %%
#Finish up by printing statement with forecast estimates below!
q_est=np.mean(q)
q_est2=np.mean(q2)
print('1 week forecast =', q_est, ', 2 week forecast = ', q_est2)

# %%
