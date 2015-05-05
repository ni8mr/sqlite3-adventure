# In this script we will prompt the user specified aggregation


import sqlite3

with sqlite3.connect("newnum.db") as conn:
    c = conn.cursor()

    prompt = """ Select the operation that you want to perform [1-5]:
    1. Average 2. Max 3. Min 4. Sum 5. Exit  -> """

    # looping until user enters a valid operation number [1-5]
    while True:
        # getting user input
        x = raw_input(prompt)

        if x in set(["1", "2", "3", "4"]):
            # parse the corresponding operation text
            operation = {1: "avg", 2: "max", 3: "min", 4: "sum"}[int(x)]

            # retrieve data
            c.execute("SELECT {}(num) from numbers".format(operation))

            # fetchone retrieves one record from the query
            get = c.fetchone()

            # just for better output
            output = {"avg": "Average", "max": "Maximum", "min": "Minimum", "sum": "Sum"}

            # outputing result to screen
            print
            print output[operation] + ": %f" % get[0]
            print
            
        elif x == "5":
            print "Exit"

            # exit loop
            break
    

