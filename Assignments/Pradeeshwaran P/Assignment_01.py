
##Basic Python

#1. Split this String

s = "Hi there Sam!"

s = "Hi there Sam!"
x=s.split()
print(x)



"""2. Use .format() to print the following string.
Output should be: The diameter of Earth is 12742 kilometers.
"""

planet = "Earth"
diameter = 12742
str=("The diameter of {planet} is {diameter} kilometers.")
print((str.format(planet="Earth",diameter=12742)))

"""3. In this nest dictionary grab the word "hello"

"""

d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}

d.get('target',{}).get('hello')

"""Numpy"""

import numpy as np

"""4.1 Create an array of 10 zeros?


4.2 Create an array of 10 fives?
"""

arr=np.zeros(10)
print(arr)

arr=np.ones(10)*5
print(arr)

"""5. Create an array of all the even integers from 20 to 35"""

arr=np.arange(20,36,2)
print(arr)

"""6. Create a 3x3 matrix with values ranging from 0 to 8"""

arr=np.arange(0,9).reshape(3,3)
print(arr)

"""7. Concatenate a and b

a = np.array([1, 2, 3]), b = np.array([4, 5, 6])
"""

a=np.array([1,2,3])
b=np.array([4,5,6])
np.concatenate((a,b),axis=None)

"""Pandas
8. Create a dataframe with 3 rows and 2 columns
"""

import pandas as pd

"""9. Generate the series of dates from 1st Jan, 2023 to 10th Feb, 2023"""

pd.date_range(start='1/1/2023', end='10/02/2023')

"""10. Create 2D list to DataFrame

lists = [[1, 'aaa', 22], [2, 'bbb', 25], [3, 'ccc', 24]]
"""

lists = [[1, 'aaa', 22], [2, 'bbb', 25], [3, 'ccc', 24]]
lst = [[1, 'aaa', 22], [2, 'bbb', 25], [3, 'ccc', 24]]    
df = pd.DataFrame(lst,columns =['Tag','day','number']) 
print(df)
