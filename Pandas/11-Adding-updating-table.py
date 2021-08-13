# adding the table
df7['Continent']=df7.shape[0]*['North America']
df7


# updating the table
df7['Continent']=df7['Country'] + ', ' + 'North America'
df7


# transposing the table
df7_t = df7.T
df7_t

