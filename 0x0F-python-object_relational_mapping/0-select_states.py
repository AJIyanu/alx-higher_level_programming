#!/usr/bin/python3
""" 
a script that lists all states from the database hbtn_0e_0_usa
"""
  
 
import MySQLdb
import sys
import pymysql
pymysql.install_as_MySQLdb()


if __name__ == "__main__":
    db = MySQLdb.connect("localhost", sys.argv[1], sys.argv[2], sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states")

    result = cursor.fetchall()
    for row in result:
        print(row)
        print()
