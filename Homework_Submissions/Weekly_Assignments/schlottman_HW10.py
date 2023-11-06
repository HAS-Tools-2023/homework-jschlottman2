### Assignment: Week 10 Python Skills Review
## Name: Jason Schlottman
## Date: 11/03/2023

# %%
# Import.
import pandas as pd
import numpy as np
import os
import urllib
import matplotlib.pyplot as plt
#from sklearn import datasets
#from sklearn.linear_model import LinearRegression

# %%
# Identify File Pathway
filename = 'streamflow_week10.txt'
filepath = os.path.join(filename) 
print(os.getcwd())
print(filepath)

#%%
### Exercise 1: 
# Given the following dataframe:
data=pd.read_table(filename, sep = '\t', skiprows=31,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code'],
                   index_col='datetime', parse_dates =['datetime']
                   )

data = np.random.rand(4, 5)
def myadd(data):
    answer = np.mean(data, axis = 0)
    return(answer)
myadd(data)

# %%
# Write a function and use it to calculate the mean of every colum of the dataframe
# If you have time try doing it with and without a for loop (You can either use the function inside your fo loop or put a for loop inside your function)
def mean_columns(my_array):
    ncol= my_array.shape[1]
    col_mean=np.zeros(5)
    for i in range(ncol):
        col_mean[i]=np.mean(my_array[:,i])
    return(col_mean)
mean_columns(data)

def take_mean(some numbers):
    mean_number = np.mean(some numbers)
    return(mean_number)
mean_columns=np.zeros(5)
for i in range(data.shape[1]):
    mean_columns[i] = take_mean(data[:,i])

#%% Exercise 2: regression analysis
# It describes measurements of sepal & petal width/length for three different species of iris
iris_df = pd.read_csv('iris_df.csv', index_col='species')

# %%
# 1. How do you view the "unique" species in the `iris_df` index?
#hint use the function np.unique() and apply it to the index of the dataframe
np.unique(iris_df.index)

# %%
# 2. How do you "locate" only rows for the `versicolor` species?
#Hint use .loc to the rows that have the name 'versicolor'
iris_df.loc['versicolor']

# %%
# 3. Calculate the mean for every column of the dataframe grouped by species. 
# look back at our pandas examples Use groupby.mean
iris_df.groupby(iris_df.index).mean()

# %%
# 4. Make a scatter plot of the `sepal length (cm)` versus the `petal length (cm)` for the `versicolor`` species?
#hint first grab out just the rows you want to plot 
#Then use scatter plot function to plot the columns you want (plotting notes)

versicolor_iris = data_frame.loc[species_name]
    versicolor_sepal = versicolor_iris[[flower_part_1]]
    versicolor_petal = versicolor_iris[[flower_part_2]]

    xVers = versicolor_sepal
    yVers = versicolor_petal

    fig, ax = plt.subplots()
    ax.scatter(xVers, yVers, marker='.',color = 'tomato')

    ax.set_xlabel('sepal length (cm)')
    ax.set_ylabel('petal length (cm)')
    ax.set_title('Versicolor Sepal Length vs Versicolor Petal Length')

    return plt.show()
# 5.  Do the same plot for `setosa` and `virginica` all on the same figure. Color them 'tomato', 'darkcyan', and 'darkviolet', respectively. (BONUS: Try to write the code so you only need to type each iris name one time)

#Repeat what you did in 4 three times


# 6. Write a function that will do 'ax.scatter' for a given iris type and desired color of points and use this to function to modify the code you make in 5

#HINT no for loop needed, the function should have two arguments and you will call it 3 times. 
#Copy your code from #5 down here and replace your ax.scatter calls with your function. 

# %%
# Exercises from Thursday's class:
# modify the following to create a pandas dataframe where the column 'datetime' is a datetime object. You should do this two ways: (1) by modifying the read.table function arguments directly. (2) keeping the read.table line I have below the same and modifying the dataframe after the fact. 
# How can you check to confirm that what you did worked? 
data = pd.read_table('streamflow_demo.txt', sep='\t',skiprows=30, names=['agency_cd', 'site_no',
                            'datetime', 'flow', 'code'])



# Exercise 2: 

# %%
#2.1: Read the 'daymet.csv' file in as a data frame using the 'date' column as the index and making sure to treat that column as a datetime object. 
daymet_df = pd.read_csv('daymet.csv', 
parse_dates =['date'], 
index_col = ['date'])
                              
print(daymet_df.info)
print(daymet_df.index)

# %%
#2.2: Explore this dataset and report what variables it contains, what date ranges are covered and the frequency of the data. 
daymet_df.shape
daymet_df.info()

daymet_df.head()
daymet_df.tail()

# %%
#2.3  Make a scatter plot of day length (dayl) vs maximum temperature.
fig, ax = plt.subplots()
fig.set_size_inches(15, 15)
ax.scatter(daymet_df['dayl (s)'], daymet_df['tmax (deg c)'])
ax.set_xlabel('Day Length (day1)')
ax.set_ylabel('Maximum Temperature (deg c)')
ax.set_title('Day Length vs. max temperature (deg c)')

# %%
