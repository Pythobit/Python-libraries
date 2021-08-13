import pandas

df1 = pandas.read_csv('supermarkets.csv')
df1


df2 = pandas.read_json('supermarkets.json')
df2


df3 = pandas.read_excel('supermarkets.xlsx',sheet_name=0)
df3

