Name: Jason Schlottman
Date: 09/19/2023
Assignment: HW Week 5 Numpy Part 2

This week's assignment focused on using conditionals and the numpy array flow_data provided in the starter code from the previous week. My 1-week and 2-week forecast values were 157.286 cfs and 309 cfs respectively. These values were attained by taking averages of the same date but on previous years to reflect a likely or probable estimate for the values of this year.

The average flow for the 5-year period was 591.1092688937568 cfs.

Printed dimensions of flow_5yr : 
[[2.015e+03 1.000e+00 1.000e+00 2.240e+02]
 [2.015e+03 1.000e+00 2.000e+00 2.200e+02]
 [2.015e+03 1.000e+00 3.000e+00 2.170e+02]
 ...
 [2.019e+03 1.200e+01 2.900e+01 7.330e+02]
 [2.019e+03 1.200e+01 3.000e+01 4.980e+02]
 [2.019e+03 1.200e+01 3.100e+01 3.880e+02]]
In addition, using np.size() returns 7304 & np.ndim() returns 2.

 Convert daily average flow value from cfs to cubic feet. For return without using a for loop I simply converted via dimensional analysis:
 cf/s * (3600s/1hr)*(24hr/1day)
 Total flow over entire time period: 51071840.832 cubic feet.
 To convert with a for loop I saved to the variable flow_daily. Below are the first 5 daily flow values:
 [19353600. 19008000. 18748800. ... 43027200. 33523200. 33523200.]

Time series of monthly average flow:
First 5 rows with each column representing year, month, & flow:
[2.015e+03 1.000e+00 0.000e+00]
 [2.016e+03 2.000e+00 0.000e+00]
 [2.017e+03 3.000e+00 0.000e+00]
 [2.018e+03 4.000e+00 0.000e+00]
 [2.019e+03 5.000e+00 0.000e+00]

Reflectio9nh & Challenges: I honestly have a bit of a hard time still with the syntax and format of numpy arrays. I was confused and had trouble, especially on the final question. I'm guessing my output is not fully correct, as although I do have values which properly reflect years and months, they are not in the correct order as well as that all flow values appear to be 0 which I have a suspicion is not the case. I'm confident however that with more practice I will improve and be more capable of approaching these challenges over time!

