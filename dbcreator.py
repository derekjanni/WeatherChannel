import pandas
import sqlite3

conn = sqlite3.connect('zipdb.db')

df = pandas.read_csv('free-zipcode-database.csv')
df.to_sql('zipcodes', conn, flavor='sqlite')

conn.commit()
conn.close()
