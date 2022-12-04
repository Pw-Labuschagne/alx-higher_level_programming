#!/usr/bin/python3
"""A scrip to display cities"""

import MySQLdb
import sys


def DisplayCities():
    """Display cities in db hbtn_0e_4_usa"""

    username = sys.argv[1]
    password = sys.argv[2]
    D_B = sys.argv[4]
    H_N = "localhost"
    p_Id = 3306

    db = MySQLdb.connect(host=H_N, user=username,
                         passwd=password, db=D_B, port=p_Id)

    cur = db.cursor()

    cur.execute("SELECT cities.id, cities.name FROM cities, states LEFT \
            WHERE state_id = states.id ORDER BY cities.id ASC")

    show = cur.fetchall()

    cur.close()
    db.close()

    for i in show:
        print(i)


if __name__ == "__main__":
    DisplayCities()
