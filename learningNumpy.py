import numpy as np
lst = [1,2,3]
lstt = np.array(lst)
print(lstt)

mtrx = [[1,2,3],[4,5,6],[7,8,9]]
npmtrx = np.array(mtrx)
print(npmtrx)
print()
#generation methods
#np.arrange(start, stop, step, dtype)
#it's just like the 'range" keyword
print(np.arange(0,11,2))
print()
#arrays of all zeroes
#good for initializing lists
#np.zeros((tuple)) rowxcol
print(np.zeros((5,4)))
''' THere is also an equivalent function for a list of ones'''
print()

#np.linspace(start,stop,number)
print(np.linspace(0,5,10))
#returns a one dimensional vector of 10 evenly spaced points from start to end
print()
#np.eye will create a nxn identity matrix
print(np.eye(5))

print()

#random methods
#Will return random numbers from zero to 1. use a comma to make a matrix
print(np.random.random(5))
print()
#random numbers from a standard distribution
print(np.random.randn(2,4) ,'me')
print()
#low, high, and number of integers
print(np.random.randint(1,100,10))


print()
print()
arr = np.arange(25)
ranarr = np.random.randint(0,50,10)
print(arr)
print(ranarr)

'''Reshape method'''
'''Give a new dimension to a matrix'''
print(arr.reshape(5,5))


'''Finding max or min values in np arrays'''
print()

print(ranarr.max())
#there's also a min
'''argmax'''
ranarr.argmax()
#returns the index location of the max or min value in a list.

arr.shape
#returns the shape in a tuple of the dimensions of an array
arr.dtype
#returns the type of the values in the matrix

'''other functions'''
mat = np.arange(1,26).reshape(5,5)

mat.sum()
mat.std()
'''Sum can be given an argument, "axis" which allows you to get the sum
of the rows or the columns
rows = 1
cols = 0'''
mat.sum(axis=1)
