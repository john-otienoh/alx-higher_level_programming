#!/usr/bin/python3
"""
script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            password=sys.argv[2],
            database=sys.argv[3],
            port=3306
        )
    cursor = db.cursor()
    cursor.execute("""SELECT cities.id, cities.name, states.name
            FROM cities INNER JOIN states ON states.id=cities.state_id""")
    results = cursor.fetchall()
    for i in results:
        print(i)
    cursor.close()
    db.close()
