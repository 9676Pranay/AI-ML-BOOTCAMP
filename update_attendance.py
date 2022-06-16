import sqlite3
c=sqlite3.connect('Bootcamp1.db')
q='''
    update attendance set name='abc' where gid=103
'''
c.execute(q)
c.commit()
c.close()