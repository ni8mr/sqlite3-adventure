# INSERT Command

"""Using the "inventory" created in sqla1.py, 
adding (`INSERT`) 5 records (rows of data) to the table. 
Make sure 3 of the vehicles are Fords while the other 2 are Hondas. 
Use any model and quantity for each."""

# import the sqlite3 library
import sqlite3


with sqlite3.connect("cars.db") as conn:
	c = conn.cursor()

	cars = [('Ford', 'Focus', 10),
	('Honda', 'Civic', 11),
	('Ford', 'Ranger', 12),
	('Honda', 'Accord', 13),
	('Ford', 'Avenger', 14)]

	c.executemany("INSERT INTO inventory VALUES(?, ?, ?)", cars)

