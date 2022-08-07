#!/usr/bin/python3
""" all states with a name starting with N (upper N) from the database """
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute(
        """SELECT c.name
        FROM states s
        INNER JOIN cities c ON s.id = c.state_id
        WHERE s.name = %s
        ORDER BY c.id""",
        [sys.argv[4]]
        )
    rows = cur.fetchall()
    print(', '.join(str(row[0]) for row in rows))
    # for row in rows:
    #     for col in row:
    #         print("%s, " % col)
    #     print('\n')
    cur.close()
    db.close()
