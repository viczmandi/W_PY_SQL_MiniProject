__author__ = 'viczmandi'


import mysql.connector

# building up db connection
db = mysql.connector.connect(user="root", password="", host="localhost", database="meetupsystemdb")

# prepare a cursor object using cursor() method
cursor = db.cursor()

try:
    for query in open("../sql_scripts/query.sql"):
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            print(row)
except Exception as ex:
    print("Error: unable to fetch data: ", ex)

# disconnect from server
db.close()