import sqlite3
c=sqlite3.connect('Bootcamp1.db')
c.execute("drop table attendance")
c.commit()
c.close()