#!/usr/bin/python3
"""Script"""

import MySQLdb
import sys


def ListStates():
    """list all states in db"""
    username = sys.argv[1]
    password = sys.argv[2]
    D_B = sys.argv[3]
    H_N = 'localhost'
    port = 3306
    db = MySQLdb.connect(host=H_N, user=username, passwd=password,
                         db=D_B, port=port)
    cur = db.cursor()
    cur.execute('SELECT * FROM states ORDER BY id ASC;')
    result = cur.fetchall()
    cur.close()
    db.close()
    if result:
        for row in result:
            print(row)


if __name__ == '__main__':
    ListStates()
