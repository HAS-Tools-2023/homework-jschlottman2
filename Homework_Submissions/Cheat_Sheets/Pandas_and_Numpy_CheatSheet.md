# Name:c Jason Schlottman
## Date: 10/30/2023
## Assignment: Pandas and Numpy Cheatsheet


### Numpy:
The general purpose of the numpy library
Numpy or Numerical Python is a widely used package for scientific computing in Python. 'It provides a multidimensional array object (n-dimensional array, denoted ndarray), as well as variations such as masks and matrices, which can be used for various mathematical operations on numerical datatypes'. 

What numpy array's are and what kinds of things they can (and can't contain)
An array is a central data structure of the NumPy library. It is a grid of values containing raw data, how to locate an element, and how to interpret an element. It has a grid of elements that can be indexed in various ways.
Various approaches for how to slice a numpy array (e.g. grabbing out a row, column, range of values)
*Source: https://www.activestate.com/resources/quick-reads/what-is-numpy-used-for-in-python/

How to create a numpy array from scratch (please show at least 2 options)
There are 6 general methods of creating arrays:

'Conversion from other Python structures (i.e. lists and tuples)

Intrinsic NumPy array creation functions (e.g. arange, ones, zeros, etc.)

Replicating, joining, or mutating existing arrays

Reading arrays from disk, either from standard or custom formats

Creating arrays from raw bytes through the use of strings or buffers'.
*Source: https://numpy.org/doc/stable/user/basics.creation.html

Typical Helpful Functions:

Linspace
Mean
Array
Reshape
Sort
Unique
Argmax and argmin
Comparing two arrays
Median
Randomize arrays
Slicing

### Pandas
The general purpose of the Pandas library
Pandas is a Python library used with data sets. The library features a multitude of tools and functions for analyzing, cleaning, exploring, and manipulating data. Data merging is simple and pandas is easy to use but still an incredibly powerful quick and efficient tool.
What makes a pandas data frame is different from a numpy array
Pandas is preffered for working with tabular data. Numpy on the other hand is suitable for working with numerical data.
The powerful tools of pandas are Data frame and Series. Whereas the powerful tool of numpy is Arrays.

An explanation of what the 'index' of a dataframe and why its different from other columns
The index of a DataFrame is a series of labels that identify each row. The labels can be integers, strings, or any other hashable type. The index is used for label-based access and alignment, and can be accessed or modified using this attribute.

How to setup a pandas dataframe by reading a file
In order to read our text file and load it into a pandas DataFrame all we need to do is use a function such as read_csv to reading file.

How to set the index of a pandas dataframe
One method is to set the index using a column. Then create pandas DataFrame. We can create a DataFrame from a CSV file or dict .
Identify the columns to set as index. We can set a specific column or multiple columns as an index in pandas DataFrame,
Use DataFrame.set_index() function.
Set the index in place.

How to slice a pandas dataframe, iloc/loc,etc.:
Sometimes generating a simple Series doesn’t accomplish our goals. For more complex operations, Pandas provides DataFrame Slicing using “loc” and “iloc” functions. We can simply slice the DataFrame created with the grades.csv file, and extract the necessary information we need.

5-6 helpful pandas functions or methods that you can use to inspect your dataframe (list each and explain what it does)
There are many very helpful pandas functions and methods available. Some common ones are: "shape, groupy,rename,iloc,sort,readcsv,etc".
