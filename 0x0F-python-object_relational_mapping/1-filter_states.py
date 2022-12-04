#!/usr/bin/python3
"""A script to list all states Starting with cap N"""

import MySQLdb
import sys


def ListStatesN():
    """lists all states with a name that starts with N"""
    username = sys.argv[1]
    password = sys.argv[2]
    D_B = sys.argv[3]
    H_N = 'localhost'
    port = 3306

    db = MySQLdb.connect(host=H_N, user=username, passwd=password,
                         db=D_B, port=port)
    cur = db.cursor()
    cur.execute('SELECT * FROM states WHERE name regexp "^N.*" ' +
                'ORDER BY states.id ASC')
    result = cur.fetchall()
    cur.close()
    db.close()
    if result:
        for row in result:
            if row[1][0] == "N":
                print(row)


if __name__ == "__main__":
    ListStatesN()
