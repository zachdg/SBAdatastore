import mysql.connector

db_conn = mysql.connector.connect(host="localhost", user="root", password="password", database="rides")

db_cursor = db_conn.cursor()

db_cursor.execute('''
            CREATE TABLE request
          (id INT NOT NULL AUTO_INCREMENT, 
           name VARCHAR(250) NOT NULL,
           location VARCHAR(250) NOT NULL,
           destination VARCHAR(250) NOT NULL,
           time VARCHAR(250) NOT NULL,
           notes VARCHAR(100) NOT NULL,
           date_created VARCHAR(100) NOT NULL,
           CONSTRAINT request_pk PRIMARY KEY (id))
          ''')

db_cursor.execute('''
            CREATE TABLE report
          (id INT NOT NULL AUTO_INCREMENT, 
           name VARCHAR(250) NOT NULL,
           customer VARCHAR(250) NOT NULL,
           pickup VARCHAR(250) NOT NULL,
           dropoff VARCHAR(250) NOT NULL,
           pickuptime VARCHAR(250) NOT NULL,
           dropofftime VARCHAR(250) NOT NULL,
           rating VARCHAR(250) NOT NULL,
           notes VARCHAR(100) NOT NULL,
           date_created VARCHAR(100) NOT NULL,
           CONSTRAINT report_pk PRIMARY KEY (id))
          ''')

db_conn.commit()
db_conn.close()