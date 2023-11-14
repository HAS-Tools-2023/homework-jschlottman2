# Assignment: HW 9 Forecast Script
## Author Name: Jason Schlottman
## Date: 10/30/2023
 
###
### Grade 7.5/9
**Code Review**
- I left comments in your code with some suggestions they all start with #LC 
Readability: 3/3 
    - Your code was very clean and easy to read. 
    - Nice commenting throughout. 
    - Clear variable names. 
Style: 2.75/3
    - Nice formatting overall but there are many linting issues that were not addressed with regards to spacing. 
Code:  1.75/3
    - I love that you have for loops but but I took of points for the following reasons: 
      - Not using datetime functionality (-0.25)
      - Not having a function defined in your cod (-0.5)
      - Not being able to run because file paths were broken (-0.5)




### Forecast Summary:
For this week's forecast I determined 1-week and 2-week forecast esimates of 103 cfs and 104 cfs. These values were determined by analyzing flow data from a dataframe as well as the use of for loops, lists, and conditional statements to select dates and value ranges of desired observations within the same month of October in previous years to serve as reasonable comparisons to estimate 1-week and 2-week flow values. 
Code Revision included using linter to fix mistakes and improve code readability. 

### Graphs:
Histogram showing flow distribution over time from streamguage dataset.

![Alt text](image.png)

Scatterplot showing distribution of flow measurements collected over time.

![Alt text](image-1.png)

 