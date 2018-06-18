import numpy as np
arr = np.arange(0,11)

print(arr[8])
print()
print(arr[1:5])
'''Indexing is just like in standard python for the 1 dimensional arrays'''

'''BROADCASTING'''
arr[0:5] = 100
print(arr)
#This set the first 5 values to  100, and left the rest of the list unchanged
print()
print()
print('Example of how numpy uses pointers, not copies')
slice_of_arr = arr[0:6]
slice_of_arr[:] = 99
print(slice_of_arr)
print(arr)
#Numpy keeps pointers, not copies. When you do slices.

'''To make a copy'''
arr_copy = arr.copy()
print()
print("Before broadcast")
print(arr)
print(arr_copy)
arr_copy[:] = 500
print()
print("After broadcast")
print(arr)
print(arr_copy)

'''Indexing of 2d arrays can be done with two brackets, or preferably one bracket
using one bracket notation, commas splice into the rows/columns.
All other splicing rules apply'''

mtrx2 = np.arange(5,46,5).reshape(3,3)
print(mtrx2)
print(mtrx2[1:,2])

'''CONDITIONAL SELETION'''
#Creates arrays of booleans based on condtion statements passed against the list
arr = np.arange(1,11)
print(arr)
print(arr > 5)

'''if you want to use a boolean array to conditionally select elemnts, it would look like this'''
bool_array = arr > 5
print(arr[bool_array])
#or
print(arr[arr<3])