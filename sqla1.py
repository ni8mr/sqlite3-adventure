# creating a new database called "cars", and add a table called "inventory"
# table has following fields: "Make", "Model" and "Quantity" with proper data-types

# importing sqlite3 module
import sqlite3

# creating a ne database "cars.db"
conn = sqlite3.connect("cars.db")

# creating a cursor for executing sql commands
c = conn.cursor()

# creating the desired table with desired fields 
c.execute("""CREATE TABLE inventory (Make TEXT, Model TEXT, Quantity INT)""")

# closing the connection with the database
conn.close()