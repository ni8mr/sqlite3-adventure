# INSERTING DATA 


# importing sqlite3 module
import sqlite3


# connecting with database with "with statement" so connection 
# will not need to be closed explicitly
with sqlite3.connect("new.db") as connection:
	# creating a cursor
	c = connection.cursor()

    # inserting single handedly
	c.execute("INSERT INTO population VALUES('New York City','NY', 8200000)")

	# inserting with executemany() method using tuple
	cities = [('Boston', 'MA', 600000),
	('Chicago', 'IL', 2700000),
	('Houston', 'TX', 2100000), ('Phoenix', 'AZ', 1500000)]

	c.executemany('INSERT INTO population VALUES(?, ?, ?)', cities)
