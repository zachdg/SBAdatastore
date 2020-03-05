import sqlite3

conn = sqlite3.connect('rides.sqlite')

c = conn.cursor()
c.execute('''
          DROP TABLE request
          ''')
c.execute('''
          DROP TABLE report
          ''')
conn.commit()
conn.close()
