import sqlite3
c=sqlite3.connect('Bootcamp1.db')
c.execute("insert into attendance values(101,'aaa',89)")
c.execute("insert into attendance values(102,'bbb',85)")
c.execute("insert into attendance values(103,'ccc',90)")
c.execute("insert into attendance values(104,'ddd',92)")

c.commit()
c.close()