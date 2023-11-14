# Assignment: Week 9 Forecast Script
# Author Name: Jason Schlottman
# Date: 10/30/2023
# Explanation: Run a few cells & generate forecast estimates.

# %%
# Import modules
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime

# %%
# Set the file name and path to where you have stored the data

# LC looks like this path doesn't work - I can't read in the data
filename = 'streamflow_week9.txt'
filepath = os.path.join('../data', filename)
print(os.getcwd())
print(filepath)

# %%
# Read in our data as a dataframe
data = pd.read_table(filename, sep='\t', skiprows=30,
                     names=['agency_cd', 'site_no',
                            'datetime', 'flow', 'code'],
                     )

# %%
# DataFrame, making the dates into a datetime object
# LC -- Note clear why you are reading in the same data twice. You should either have this block or the one above it. 
data2 = pd.read_table(filename, sep='\t', skiprows=30,
                      names =['agency_cd', 'site_no',
                              'datetime', 'flow', 'code'],
                              parse_dates =['datetime']
                      )

# %%
#Expand dates to day,month,year
# LC - You should use the datetime functionality instead of splitting the dates up like this. In Data2 you have them parsed as dates so you could just use that. 
data[["year", "month", "day"]] =data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)

# %%
#make lists of the data
# LC -- This is technically okay but would be much cleaner just to stick with the dataframe than to convert everything to lists. Its not clear to me what the value added of that would be. 
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
# Identify flow values in October of previous years less than 90 cfs to relate to average historical observed values.

# LC - nice use of for loops!
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
