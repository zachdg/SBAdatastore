import mysql.connector

db_conn = mysql.connector.connect(host="ec2-52-36-5-246.us-west-2.compute.amazonaws.com", user="root", password="password", database="rides")


db_cursor = db_conn.cursor()

db_cursor.execute('''
          DROP TABLE request, report
          ''')

db_conn.commit()
db_conn.close()
