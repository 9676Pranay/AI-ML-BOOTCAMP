import sqlite3
c=sqlite3.connect('Bootcamp1.db')
#q=pragma table_info(participants)
str=c.execute("pragma table_info('attendance')")
print(str)
for i in str:
    print(i)