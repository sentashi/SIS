import sqlite3
con = sqlite3.connect('baza.db')

cur = con.cursor()

# Create table
cur.execute('''CREATE TABLE IF NOT EXISTS user
               (id integer primary key, name text, email text, password text, contact text, created_at text, login_count integer DEFAULT 0)''')

con.commit()
con.close()
