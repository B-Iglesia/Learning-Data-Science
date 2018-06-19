import pandas as pd
import numpy as np
from numpy.random import randn
'''Data frames built off of SERIES'''
np.random.seed(101)
'''Data frames have data, index, columns, dtype, and copy as arguments'''
'''Dataframes are basically series that share indices'''
df = pd.DataFrame(randn(5,4),['A','B','C','D','E'], ['W','X','Y','Z'])
print(df)

print()
print(df['W'])
print(type(df['W']))

print()
print(df.W)
'''probably don't use df.W to reference the w column as it could be overwritten by a column name'''
print()
print(df[['W','Z']])
print()

'''Can create new columns like adding new items into a dictionary. Arithmetic of series is like simple matrix addition'''
df['new'] = df['W'] + df['Y']
print(df['new'])
print()

'''df.drop will remove a column from the dataframe, but it doesn't actually get rid of the data. Visually, it is gone'''
df.drop('new',axis=1,inplace=True)
print(df)
print()
'''Can also drop rows'''
df.drop('E',inplace=False)
print(df)
print()

'''Getting the columns of a dataframe is as easy as just passing in the column label'''

'''Using df.loc[] will give a rows values by passing in the row name'''
print(df.loc['C'])
'''or'''
print()
print(df.iloc[2])

print()
'''This is like doing row,col notation'''
print(df.loc['B','W'])
print()
print(df.loc[['A','B'], ['W','Y']])


'''Conditional selection and multiindexing'''
print()
booldf = df > 0
print(df[booldf])
'''or'''
print()
print(df[df>0])
print()
print(df['W']>0)
print()
print(df[df['W']>0])


print()
print()
print(df[df['Z']>0])
'''THis statement and the one directly below are equivalent'''
res = df[df['W']>0]
print()
print(res['X'])
'''Stacked bracket notation to get the X column, but without the C column by the boolean list of W > 0'''
print()
print(df[df['W']>0]['X'])

'''multiple conditions'''
#instead of and, use &, instead of or use |
print()
print(df[(df['W']>0) & (df['Y']<0)])

'''RESETTING INDICES'''
'''Resets indices to being integer values instead of the labeled names'''
'''to make it an actual change in the dataframe, set inplace=True'''
print()
print(df.reset_index())

print()
newind = 'CA NY WY OR CO'.split()
print()
df['State'] = newind
print(df)
print()
#df.set_index('State',inplace=True)
print(df)




'''HIERARCHY and multiindexing'''
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
'''MultiIndex allows for a multiindex of items, in this case, tuples'''
hier_index = pd.MultiIndex.from_tuples(hier_index)

df = pd.DataFrame(randn(6,2),hier_index,'A B'.split())
print(df)
print()
df.index.names = ['Groups','Num']
print(df)

'''cross section'''
'''Used for multi level index to get a cross section of a data frame'''
print()
'''Get's all of the values within a slice of the dataframe based on the idexes passed'''
'''You can select a specific index to look at or specific sections to search for to look for values in the table'''
print(df.xs(1,level='Num'))
print()
print(df.xs('G1',level='Groups'))
