#!/usr/bin/python3

"""A script that lists all states in db hbtn_0e_0_usa"""

import sys
import MySQLdb


def ListStates():
    """Lists all the states in db hbtn_0e_0_usa"""
    
    db = MySQLdb.connect(host="localhost", user=sys.arg[1], passwd=sys.arg[2],
                         db=sys.arg[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY ID")
    Results = cur.fetchall()

    if Results:
        for row in Results:
            print(row)

    cur.close()
    db.close()

    if __name__ == "__main__":
        ListStates()
