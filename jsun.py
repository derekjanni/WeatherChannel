__author__ = 'derekjanni'
import weatherdata
import json

cities = [
    ('PORTLAND', 'OR'),
    ('HOUSTON', 'TX'),
    ('NEW YORK CITY', 'NY'),
    ('SEATTLE', 'WA'),
    ('LOS ANGELES', 'CA'),
    ('DENVER', 'CO'),
    ('CHICAGO', 'IL'),
    ('BOSTON', 'MA'),
    ('ATLANTA', 'GA'),
]

cities = [('PORTLAND', 'OR')]
points = {}

for i in cities:
    data = weatherdata.get(i[0], i[1])
    for x in data:
        points[str(x[0]) + ' ' + str(x[1])] = {'lat': x[0], 'long': x[1], 'temp': x[2]}


with open('data.json', 'w') as outfile:
    json.dump(points, outfile)