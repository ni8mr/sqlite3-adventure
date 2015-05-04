# Updating the quantity on two of records in "inventory"
# Outputing all of records from "inventory"

import sqlite3

with sqlite3.connect("cars.db") as conn:
    c = conn.cursor()

    c.execute("UPDATE inventory SET Quantity = 30 WHERE Model='Accord'")
    c.execute("UPDATE inventory SET Quantity = 18 WHERE Model='Avenger'")

    c.execute("SELECt * FROM inventory")

    rows = c.fetchall()

    for row in rows:
        print row[0], row[1], row[2]
