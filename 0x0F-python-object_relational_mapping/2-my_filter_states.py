#!/usr/bin/python3
"""script that takes in an argument and displays all values in the states 
table of hbtn_0e_0_usa where name matches the argument
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            password=sys.argv[2],
            database=sys.argv[4],
            state_name=sys.argv[5],
            port=3306
        )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states")
    results = cursor.fetchall()
    for i in range(len(results)):
        if state_name in results[i]:
            print(results[i]
    cursor.close()
    db.close()
