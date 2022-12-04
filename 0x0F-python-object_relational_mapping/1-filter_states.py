#!/usr/bin/python3
"""A script that lists states starting with Cap N in database hbtn_0e_0_usa"""

import sys
import MySQLdb
import re


def ListStateN():
    """Lists states with Cap N"""

    db = MySQLdb.connect(host="localhost", user=sys.arg[1], passwd=sys.arg[2], db=sys.arg[3], port=3306)

    cur = db.cursor()
    States = curr.execute('SELECT * FROM states WHERE name
                                regexp "^N.*" ORDER BY ID')

    Results = curr.fetchall()

    for row in Results:
        print(row)

    cur.close()
    db.close()

if __name__ == "__main__":
    ListStateN
