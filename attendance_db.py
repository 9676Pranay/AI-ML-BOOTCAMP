import sqlite3
c=sqlite3.connect('Bootcamp1.db')
q='''
    create table attendance(gid int primary key,name text not null)
'''

c.execute(q)