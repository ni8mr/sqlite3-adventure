# Database "new.db"
# For working with multiple table adding more data to 'population' table
# And creating another table 'regions'

import sqlite3

with sqlite3.connect("new.db") as conn:
    c = conn.cursor()

    # inserting multiple records using a tuple
    cities = [('Boston', 'MA', 600000),
              ('Los Angeles', 'CA', 38000000),
              ('Houston', 'TX', 2100000),
              ('Philadelphia', 'PA', 1500000),
              ('San Antonio', 'TX', 1400000),
              ('San Diego', 'CA', 130000),
              ('Dallas', 'TX', 1200000),
              ('San Jose', 'CA', 900000),
              ('Jacksonville', 'FL', 800000),
              ('Indianapolis', 'IN', 800000),
              ('Austin', 'TX', 800000),
              ('Detroit', 'MI', 700000)]

    c.executemany("INSERT INTO population VALUES(?, ?, ?)", cities)

    c.execute("""CREATE TABLE regions (city TEXT, region TEXT)""")

    cities1= [('New York City', 'Northeast'),
              ('San Francisco', 'West'),
              ('Chicago', 'Midwest'),
              ('Houston', 'South'),
              ('Phoenix', 'West'),
              ('Boston', 'Northeast'),
              ('Los Angeles', 'West'),
              ('Houston', 'South'),
              ('Philadelphia', 'Northeast'),
              ('San Antonio', 'South'),
              ('San Diego', 'West'),
              ('Dallas', 'South'),
              ('San Jose', 'West'),
              ('Jacksonville', 'South'),
              ('Indianapolis', 'Midwest'),
              ('Austin', 'South'),
              ('Detroit', 'Midwest')]

    c.executemany("INSERT INTO regions VALUES(?, ?)", cities1)

    # Now let's see the input of two table's here
    print "The 'population' table: "
    print
    
    c.execute("SELECT * FROM population")
    rows = c.fetchall()


    for r in rows:
        print r[0], r[1], r[2]


    print
    print "The 'regions' table: "
    print
    
    c.execute("SELECT * FROM regions")
    rows1 = c.fetchall()


    for r in rows1:
        print r[0], r[1]

    
    
