#!/usr/bin/python3
"""A script that lists states starting with Cap N in database hbtn_0e_0_usa"""

import sys
import MySQLdb
import re


if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.arg[1], passwd=sys.arg[2], db=sys.arg[3])

    cur = db.cursor()

    States = cur.execute('SELECT * FROM states WHERE name
                                regexp "^N.*" ORDER BY ID')

    Results = cur.fetchall()

    for row in Results:
        print(row)

    cur.close()
    db.close()
