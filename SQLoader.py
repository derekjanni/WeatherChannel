__author__ = 'derekjanni'
import sqlite3
import csv

#code snippets that interact with SQLite should go at top
conn = sqlite3.connect('example.db')
c = conn.cursor()
'''
c.execute(CREATE TABLE anscombe
             (x1 real, x2 real, x3 real, x4 real, y1 real, y2 real, y3 real, y4 real))
'''

#code that loads csv file as rows
with open('anscombe.csv') as csvfile:
    csv = csv.reader(csvfile)
    for row in csv:
        #print(row)

        c.execute("INSERT INTO anscombe (x1, x2, x3, x4, y1, y2, y3, y4) "
                  "VALUES (?, ?, ?, ?, ?, ?, ?, ?);", row)


'''# Create table
#c.execute({triple quotes go here} CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real){triple quotes go here})

# Insert a row of data
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

c.execute(CREATE TABLE anscombe
             (x1 real, x2 real, x3 real, x4 real, y1 real, y2 real, y3 real, y4 real))

# Larger example that inserts many records at a time
purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
             ('2006-04-0anscombe.csv5', 'BUY', 'MSFT', 1000, 72.00),
             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
            ]
c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)

for row in c.execute('SELECT * FROM stocks ORDER BY price'):
        print(row)'''


for row in c.execute('SELECT * FROM anscombe'):
        print(row)
c.execute('DELETE FROM stocks')
c.execute('DELETE FROM anscombe')

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
