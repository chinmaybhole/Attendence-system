import sqlite3 as sql

#conn = sql.connect(':memory:') create a database in memory andd disappear after we end the code
conn = sql.connect('people.db') # Create the database