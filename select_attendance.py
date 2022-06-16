import sqlite3
c=sqlite3.connect('Bootcamp1.db')
r=c.execute("select * from attendance")
for i in r:
    print(i)