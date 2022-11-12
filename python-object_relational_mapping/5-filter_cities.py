#!/usr/bin/python3
"""ORM SCRIPT"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect("localhost", sys.argv[1], sys.argv[2], sys.argv[3])
    c = db.cursor()
    c.execute("""SELECT cities.name FROM cities
            LEFT JOIN states ON states.id = cities.state_id
            WHERE states.name = %s ORDER BY cities.id ASC""", (sys.argv[4], ))
    result = c.fetchall()

    cities = ""
    sep = ""
    for i in result:
        cities = cities + sep + i
        sep = ", "
    print(cities)
