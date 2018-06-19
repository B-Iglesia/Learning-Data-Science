import numpy as np
import pandas as pd

labels = ['a','b','c']
my_data = [10,20,30]
arr = np.array(my_data)
d = {'a':10,'b':20,'c':30}
'''Creating a series using specific labels'''
sr = pd.Series(data = my_data)
print(sr)
print()
lb = pd.Series(data=my_data,index=labels)
print(lb)
print()
'''Making a series using just a numpy array'''
smp = pd.Series(arr)
print(smp)
print()
'''making a series using a dictionary'''
ds = pd.Series(d)
print(ds)

'''Series can hold almost any object'''
print()
print(pd.Series(data=labels))
print()

ser1 = pd.Series([1,2,3,4],['USA', "Germany", "USSR", "Japan"])
print(ser1)
print()

ser2 = pd.Series([1,2,5,4],["USA", "Germany", "Italy", "Japan"])
print(ser2)
print()
print(ser1['Germany'])
print()
ser3 = pd.Series(data=labels)
print(ser3[0])

print()
print(ser1 + ser2)