
# Creating a table and populate it with data for applying joining method 
# in "cars.db" 

"""Adding another table to accompany "inventory" table called "orders". 
This table have the following fields: "make", "model", and "order_date". 
Including only makes and models for the cars found in the inventory table. 
Adding 15 records (3 for each car), each with a separate order date (YYYY-MM-DD)."""

import sqlite3

with sqlite3.connect("cars.db") as conn:
	c = conn.cursor()

	c.execute("""CREATE TABLE orders
		(make TEXT, model TEXT, order_date DATE)""")

	orders = [('Ford', 'Focus', '2014-01-22'),
            ('Ford', 'Focus', '2014-01-23'),
            ('Ford', 'Focus', '2014-01-24'),
            ('Honda', 'Civic', '2014-01-25'),
            ('Honda', 'Civic', '2014-01-26'),
            ('Honda', 'Civic', '2014-01-27'),
            ('Ford', 'Ranger', '2014-01-28'),
            ('Ford', 'Ranger', '2014-01-22'),
            ('Ford', 'Ranger', '2014-01-23'),
            ('Honda', 'Accord', '2014-01-24'),
            ('Honda', 'Accord', '2014-01-25'),
            ('Honda', 'Accord', '2014-01-26'),
            ('Ford', 'Avenger', '2014-01-27'),
            ('Ford', 'Avenger', '2014-01-28'),
            ('Ford', 'Avenger', '2014-01-22')]
	c.executemany("INSERT INTO orders VALUES(?, ?, ?)".orders)

	# Let's see our table
	c.execute("SELECT * FROM orders ORDER BY order_date ASC")

	rows = c.fetchall()

	for r in rows:
            print r[0], r[1], r[2]

