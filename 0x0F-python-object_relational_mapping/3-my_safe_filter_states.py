#!/usr/bin/python3
"""Lets call it a safe way to display content"""

import MySQLdb
import sys


def SaferWay():
    """SQL injection safe"""

    username = sys.argv[1]
    password = sys.argv[2]
    D_B = sys.argv[3]
    searched = sys.argv[4]
    H_N = "localhost"
    p_Id = 3306

    db = MySQLdb.connect(host=H_N, user=username, passwd=password,
                         db=D_B, port=p_Id)

    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id",
                [searched])

    show = cur.fetchall()
    cur.close()
    db.close()

    for row in show:
        print(row)


if __name__ == "__main__":
    SaferWay()
