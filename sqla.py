# Creating a SQLite3 database and table

# importing the sqlite3 library
import sqlite3

# Creating a new database if it doesn't exist
connection = sqlite3.connect("new.db")


# getting a cursor object used to execute SQL commands 
cursor = connection.cursor()

# creating a table
cursor.execute("""CREATE TABLE population_stat (city TEXT, state TEXT, population INT)""")


# closing the database
connection.close()