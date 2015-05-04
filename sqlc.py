# SELECT statement  with and without unicode characters

import sqlite3

with sqlite3.connect("new.db") as conn:
	c = conn.cursor()

	print "with unicode characters"
	print 

	# using a for loop to iterate through the database, printing the
	# results line by line
	for row in c.execute("SELECT * FROM population"):
		print row


	print
	print "without unicode characters"
	print 

	c.execute("SELECT * FROM population")

	# fetchall() retrieves all records from the query
	rows = c.fetchall()

	# output the rows to the screen, row by row

	for r in rows:
		print r[0], r[1]

