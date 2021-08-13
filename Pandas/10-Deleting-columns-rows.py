df6.drop('City',1)

df6.drop('3995 23rd St', 0)

# updating the table
df7 = df6.drop('3995 23rd St',0)
df7

df7.drop(df7.index[0:3], 0)

df7.drop(df7.columns[0:3], 1)

df7.index

df7.columns

