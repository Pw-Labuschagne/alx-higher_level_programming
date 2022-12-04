#!/usr/bin/python3

"""A script that lists all states in db hbtn_0e_0_usa"""

import sys
import MySQLdb


if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.arg[1], passwd=sys.arg[2],
                         db=sys.arg[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY ID")
    Results = cur.fetchall()

    if Results:
        for row in Results:
            print(row)

    cur.close()
    db.close()
