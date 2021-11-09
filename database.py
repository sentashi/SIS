import sqlite3
con = sqlite3.connect('baza.db')

cur = con.cursor()

# Create table
cur.execute('''CREATE TABLE IF NOT EXISTS user
               (id int primary key, name text, email text, password text, contact text, created_at text)''')
# Insert a row of data
cur.execute("INSERT INTO user VALUES ('1', 'Andro','andro@outlook.hr','lozinka123', '+385986473846', '09112021')")


con.commit()
con.close()
