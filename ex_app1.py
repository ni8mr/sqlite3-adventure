"""We need to create a database having 100 random integers ranging from 0 to 100.
Then we will propt the user whether he or she would like to perform an aggregation(AVG,MAX,
MIN, or SUM) or exit the program altogether"""

# In this script, we will create the database and the table with random numbers


# importing necessary modules
import sqlite3
import random


with sqlite3.connect("newnum.db") as conn:
    c = conn.cursor()

    # Dropping table if it exists
    c.execute("DROP TABLE if exists numbers")

    # Creating a brand new table
    c.execute("CREATE TABLE numbers(num INT)")

    # inserting randomly generated numbers between 0 and 100 into the table
    for i in range(100):
        c.execute("INSERT INTO numbers VALUES(?)",(random.randint(0,100),))

    # Let's see what we have done here
    c.execute("SELECT * FROM numbers")

    rows = c.fetchall()

    for r in rows:
        print r[0]
