__author__ = 'viczmandi'

import mysql.connector

# building up db connection
db = mysql.connector.connect(user="root", password="", host="localhost", database="meetupsystemdb")

# prepare a cursor object using cursor() method
cursor = db.cursor()

try:
    for row in open("../sql_scripts/insert.sql"):
        cursor.execute(row)
    db.commit()
except:
    db.rollback()

# disconnect from server
db.close()