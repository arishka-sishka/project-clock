# База данных
import datetime
import sqlite3

con = sqlite3.connect("base.db")
cur = con.cursor()

cur.execute('insert into alarms(id, time, state) values(?, ?, ?)',
            (1, datetime.time(hour=0), False))
con.commit()
