# Dealing and importing from CSV

import csv

import sqlite3

with sqlite3.connect("new.db") as conn:
    c = conn.cursor()

    # opening the csv file and assign it to a variable
    employees = csv.reader(open("employees.csv", "rU"))

    # Creating a new table called employees
    c.execute("CREATE TABLE employees(firstname TEXT, lastname TEXT)")

    # inserting data
    c.executemany("INSERT INTO employees(firstname, lastname) values(?, ?)", employees)



    
