import sqlite3
c=sqlite3.connect('Bootcamp1.db')
q='''
alter table attendance add column percent int not null
'''

c.execute(q)
c.commit()