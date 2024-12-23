import sqlite3
conn = sqlite3.connect("myDB.db")
cur = conn.cursor()
req = "insert into students (nom, email, age) values ('Albert', 'albert@gmail.com', '22')"
cur.execute(req)
conn.commit()
conn.close()
