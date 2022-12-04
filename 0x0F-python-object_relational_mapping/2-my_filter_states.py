#!/usr/bin/python3
"""A script that displays if name matches argument"""

import MySQLdb
import sys

def Matched():
    """Prints if it matches"""

    username = sys.arg[1]
    password = sys.arg[2]
    D_B = sys.arg[3]
    searched = sys.argv[4]
    H_N = "localhost"
    p_Id = 3306

    db = MySQLdb.connect(host=H_N, user=username, passwd=password, db=D_B, port=p_Id)

    cur = db.cursor()

    cur.execute(("SELECT * FROM states WHERE BINARY name = \'{}\'\ ORDER
                BY id").format(searched))

    show = cur.fetchall()

    for row in show:
        print(show)

    cur.close()
    db.close()


if __name__ == "__main__":
    Matched()
