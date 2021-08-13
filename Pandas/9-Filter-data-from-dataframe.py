"""
Two ways - Label based indexing, position based indexing
"""

# for label indexing
df6.loc['735 Dolores St':'3995 23rd St','City':'Name']


# for a specific address city
df6.loc['735 Dolores St','City']


# for all cities
df6.loc[:,'City']


list(df6.loc[:,'City'])


# for position indexing, we use iloc
df6.iloc[1:3, 1:3]

# here 3 will not be included as it is upper bound exclusive

df6.iloc[3, 1:4]
