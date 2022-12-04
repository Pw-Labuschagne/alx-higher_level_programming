#!/usr/bin/python3
"""A script list all cities where states is an argument"""

import MySQLdb
import sys


def ListByState():
    """lists all cities as states argument"""

    username = sys.argv[1]
    password = sys.argv[2]
    D_B = sys.argv[3]
    state_name = sys.argv[4]
    H_N = 'localhost'
    p_Id = 3306

    db = MySQLdb.connect(host=H_N, user=username, passwd=password,
                         db=D_B, port=p_Id)
    cur = db.cursor()

    cur.execute('SELECT c.name FROM cities c INNER JOIN states s ' +
                'ON s.id = c.state_id WHERE ' +
                'BINARY s.name = %s ' +
                'ORDER BY c.id ASC;', [state_name])
    show = cur.fetchall()
    cur.close()
    db.close()

    print(', '.join(map(lambda x: x[0], show)))


if __name__ == '__main__':
    ListByState()
