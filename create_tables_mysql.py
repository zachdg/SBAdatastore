import mysql.connector

# conn = mysql.connector.connect(host="ec2-52-36-5-246.us-west-2.compute.amazonaws.com", user="root", password="password")
# c = conn.cursor()
# c.execute("CREATE DATABASE rides")
# conn.commit()
# conn.close()

db_conn = mysql.connector.connect(host="ec2-34-223-239-244.us-west-2.compute.amazonaws.com", user="user", password="password", database="rides")

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
