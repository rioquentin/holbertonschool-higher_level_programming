#!/usr/bin/python3
"""ORM SCRIPT"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect("localhost", sys.argv[1], sys.argv[2], sys.argv[3])
    c = db.cursor()
    c.execute("""SELECT cities.id, cities.name, states.name FROM cities
            LEFT JOIN states ON cities.state_id = states.id
            ORDER BY cities.id ASC""")
    result = c.fetchall()

    for i in result:
        print(i)
