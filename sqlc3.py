# Outputing only records from "inventory" that are 'Ford' vehicles

import sqlite3

with sqlite3.connect("cars.db") as conn:
    c = conn.cursor()

    c.execute("SELECT * FROM inventory WHERE Make='Ford'")

    rows = c.fetchall()

    for row in rows:
        print row[0], row[1], row[2]
