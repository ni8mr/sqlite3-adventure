# Joining data from multiple tables
# In our case, 'population' and 'regions' table from 'new.db'

import sqlite3

with sqlite3.connect("new.db") as conn:
    c = conn.cursor()

    # retrieve data
    c.execute("""SELECT population.city, population.population,
            regions.region FROM population, regions
            WHERE population.city = regions.city""")

    rows = c.fetchall()

    for r in rows:
        print r[0], r[1], r[2]
