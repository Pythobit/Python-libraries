import pandas

df1 = pandas.DataFrame([[2, 4, 6], [10, 20, 30]])
df2 = pandas.DataFrame([[2, 4, 6], [10, 20, 30]], columns=['Price', 'Age', 'Value'], index=['First', 'Second'])
df3 = pandas.DataFrame([{'Name': 'John'}, {'Name': 'Jack'}])
df4 = pandas.DataFrame([{'Name': 'John', 'Surname': 'Jacobs'}, {'Name': 'Jack'}])


print(df1)
# mean of each value in the dataframe
print(df1.mean())
# mean for the whole dataframe
print(df1.mean().mean())
# type class of dataframe
print(type(df1))

print('\n')
print(df2)
print(df2.Price.mean())
print(df2.Price.max())
print(df2.Price.min())

print('\n')
print(df3)

print('\n')
print(df4)
