from geopy.geocoders import ArcGIS
arc = ArcGIS()

value = arc.geocode('3666 21st St, San Francisco, CA 94114')
value

print(value.longitude)
print(value.latitude)

import pandas
df = pandas.read_csv('supermarkets.csv')
df

df['Address'] = df['Address'] + ', ' + df['City'] + ', ' + df['State'] + ', ' + df['Country']
df

df['Co-ordinates'] = df['Address'].apply(arc.geocode)
df

df['Latitude'] = df['Co-ordinates'].apply(lambda x: x.latitude)
df['Longitude'] = df['Co-ordinates'].apply(lambda x: x.longitude)
df

