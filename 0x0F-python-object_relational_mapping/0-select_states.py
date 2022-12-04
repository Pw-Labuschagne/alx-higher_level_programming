#!/usr/bin/python3

"""A script that lists all states in db hbtn_0e_0_usa"""

import sys
import MySQLdb


def ListStates():
    """Lists all the states in db hbtn_0e_0_usa"""

    username = sys.arg[1]
    password = sys.arg[2]
    dbName = sys.arg[3]
    host_name = 'localhost'
    port_id = 3306
    
    db = MySQLdb.connect(host=host_name, user=username, passwd=password,
                         db=dbName, port=port_id)

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY ID ASC;")
    Results = cur.fetchall()
    cur.close()
    db.close()

    if Results:
        for row in Results:
            print(row)

    if __name__ == "__main__":
        ListStates()
