import sqlite3
c=sqlite3.connect('Bootcamp1.db')

c.execute("delete from attendance where name='ddd'")
print(c.total_changes)
c.commit()
c.close()