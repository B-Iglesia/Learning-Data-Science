'''Numpy has some basic scallar operations that can act on the arrays'''
import numpy as np
arr = np.arange(0,10)
'''Vector adds(subs) the arrays together'''
arr + arr
arr - arr
'''This multiplication is not like in linear, it multiplies each array by their respective index'''
arr * arr
'''If there is a zero value, instead of returning an error, it will place a NaN in it's place'''
arr / arr
'''If there is a 0, it will put inf in it's place '''
1/arr
'''Self explanatory power usage'''
arr**3 
'''Returns the square root of each value in the array'''
np.sqrt(arr)
'''returns the value of e^ of each value'''
np.exp(arr)

'''max,min,log,sin, etc are also possibilites'''