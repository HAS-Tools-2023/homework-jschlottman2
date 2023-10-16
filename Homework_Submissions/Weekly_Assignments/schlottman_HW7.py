# Python file for Assignment #7 Matplotlib
# Name: Jason Schlottman
# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# Set the file name and path to where data is stored.
filename = 'streamflow_week7.txt'
filepath = os.path.join('../../data', filename)
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
# StreamGuage Data Output
print(data)
print(data.index)
print(data.info())
print(data.describe())

#Produced 5 plots with code below

# %%
# Line plot produced with Pandas Dataframe
df=pd.DataFrame(data)
df.plot.line(x='datetime', y='flow')
plt.xlabel("Dates")
plt.ylabel('Flow')
plt.title('Observed Flow for 20-year Period')

# %%
# Scatter plot
df=pd.DataFrame(data)
df.plot.scatter(x='datetime', y='flow', color='pink')
plt.xlabel("Time")
plt.ylabel('Flow')
plt.title('Observed Flow Over Time')

# %%
#Bar Plot:
df=pd.DataFrame(data)
df.plot.bar(x='datetime', y='flow', color='magenta')
plt.xlabel("Dates")
plt.ylabel('Flow (cfs)')
plt.title('Flow Observations Pattern Over Time ')

# %%
# Histogram:
Z=np.random.normal(0, 1, 100)
plt.xlabel('Datetime')
plt.ylabel('Flow Observations')
plt.title('Flow Distribution Across Time Histogram')
plt.hist(Z)

# %%
#Multiplot, displays flow over two selected distinct periods of time to provide insight into distribution of flow data over certain timescales.
x='datetime'
fig, (ax1, ax2) =plt.subplots((2))
ax1.plot(x, y, color='turquoise')
ax2.plot(np.mean(x), y, color='yellow')
ax.set_ylabel("Flow")
ax.set_xlabel('time')
ax.set_title("Flow over Two Distinct Time Periods")
fig.show()
# %%
