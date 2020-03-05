import sqlite3

conn = sqlite3.connect('rides.sqlite')

c = conn.cursor()
c.execute('''
          CREATE TABLE request
          (id INTEGER PRIMARY KEY ASC, 
           name VARCHAR(250) NOT NULL,
           location VARCHAR(250) NOT NULL,
           destination VARCHAR(250) NOT NULL,
           time VARCHAR(250) NOT NULL,
           notes VARCHAR(100) NOT NULL,
           date_created VARCHAR(100) NOT NULL)
          ''')

c.execute('''
          CREATE TABLE report
          (id INTEGER PRIMARY KEY ASC, 
           name VARCHAR(250) NOT NULL,
           customer VARCHAR(250) NOT NULL,
           pickup VARCHAR(250) NOT NULL,
           dropoff VARCHAR(250) NOT NULL,
           pickuptime VARCHAR(250) NOT NULL,
           dropofftime VARCHAR(250) NOT NULL,
           rating VARCHAR(250) NOT NULL,
           notes VARCHAR(100) NOT NULL,
           date_created VARCHAR(100) NOT NULL)
          ''')

conn.commit()
conn.close()
