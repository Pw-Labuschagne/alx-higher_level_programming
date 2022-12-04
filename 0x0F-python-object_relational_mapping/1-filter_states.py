#!/usr/bin/python3
"""A script that lists states starting with Cap N in database hbtn_0e_0_usa"""

import MySQLdb
import sys


def ListStatesN():

    H_N = "localhost"
    p_Id = 3306
    username = sys.argv[1]
    password = sys.argv[2]
    D_B = sys.argv[3]

    db = MySQLdb.connect(host=H_N, port=p_Id, user=username, passwd=password, db=D_B)

    cur = db.cursor()

    cur.execute('SELECT * FROM states WHERE name
                                regexp "^N.*" ORDER BY ID')

    Results = cur.fetchall()

    for row in Results:
        print(row)

    cur.close()
    db.close()

if __name__ == "__main__":
    ListStatesN()
