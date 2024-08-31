'''
1. Convert the below list into numpy array then display the array 

Input: my_list = [1, 2, 3, 4, 5] 
'''

import numpy as np
my_list=[1,2,3,4,5]
my_array=np.array(my_list)
print(my_array)

'''
2. Convert the below list into a numpy array then display the array then display the first and last index and then multiply each element by 2 and display the result. 

Input: my_list = [1, 2, 3, 4, 5]
'''

my_list=[1,2,3,4,5]
my_array=np.array(my_list)
print(my_array)
print("First Element: ",my_array[0])
print("Second Element: ",my_array[1])
my_array = my_array*2
print("Array after doubling each element:\n",my_array)

'''
Lab3 : Working with Numpy using Jupyter 

1. Write a NumPy program to create an array of 10 zeros, 10 ones, and 10 fives.  
'''

arr_zeros = np.zeros(10)
arr_ones = np.ones(10)
arr_fives = np.ones(10)*5
print("Array of 10 Zeros:\n",arr_zeros)
print("Array of 10 Ones:\n",arr_ones)
print("Array of 10 Fives:\n",arr_fives)

'''
2. Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.
'''

mat = np.arange(2,11).reshape(3,3)
print(mat)