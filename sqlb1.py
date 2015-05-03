# Insert command with error handler


# importing sqlite3 module
import sqlite3


# connecting with database with "with statement" so connection 
# will not need to be closed explicitly
with sqlite3.connect("new.db") as connection:
	# creating a cursor
	c = connection.cursor()

	# inserting with executemany() method using tuple
	cities = [('Boston', 'MA', 600000),
	('Chicago', 'IL', 2700000),
	('Houston', 'TX', 2100000), ('Phoenix', 'AZ', 1500000)]
	try:
		c.executemany('INSERT INTO populations VALUES(?, ?, ?)', cities)
	except sqlite3.OperationalError:
		print "Oops! Something wen wrong. Try again . . ."
