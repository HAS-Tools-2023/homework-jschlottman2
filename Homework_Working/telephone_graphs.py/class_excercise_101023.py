
#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

## Import the flow data to use
data = pd.read_table("./streamflow_demo.txt", sep='\t', skiprows=30, names=['agency_cd', 'site_no', 'datetime', 'flow', 'code'])
data[["year", "month", "day"]] = data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)
# %%
#Plot 2 changed colormap from viridis to magma.
ax=data.plot.scatter(x='month', y='flow',
c='year', colormap='magma', marker='x')
ax.set_title("Monthly stream Flow")
# %%
# Plot 1
x = np.linspace(-5 * np.pi, 5 * np.pi, 1000)
y1=np.sin(x)
y2=np.cos(x)
ax = plt.axes()
ax.plot(x, y1, linestyle='dotted', label='sinx')
ax.plot(x, y2, linestyle='dashed', color='green', label='cosx')
ax.set_title('cos(x) vs. sin(x)')
ax.legend(loc='upper right')
# %%
monthly_max = data.groupby(data.month).max()
monthly_min = data.groupby(data.month).min()
monthly_mean = data.groupby(data.month)["flow"].mean()

ax = plt.axes()
ax.plot(monthly_mean, label='monthly mean')
ax.fill_between(monthly_min.flow.index,
monthly_min.flow.values, monthly_max.flow.values, alpha=0.2, label=’Area between min and max’)
ax.set_yscale("log")
ax.set_xlabel("month")
plt.axvline(3, color='black', linestyle='--', label=’March’)
ax.legend()

# %%
