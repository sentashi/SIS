import sqlite3
from hashlib import blake2b
con = sqlite3.connect('baza.db')

def register_user(email, lozinka):
    cur = con.cursor()
    
    h = blake2b()
    transbyte = str.encode(lozinka)
    h.update(transbyte)
    #ovo je lozinka
    print(transbyte)
    print(h.hexdigest())
    cur.execute("INSERT INTO user (email, password) VALUES (?, ?);", (email, h.hexdigest()))
    con.commit()
    con.close()

def login(email, lozinka):
    cur = con.cursor()
    
    h = blake2b()
    transbyte = str.encode(lozinka)
    h.update(transbyte)
    
    print(email)
    cur.execute("SELECT * FROM user WHERE email= ?;", (email,))
    podaci= cur.fetchone()
    
      

    if podaci[3]==h.hexdigest():
        print("Uspjesan login")

        rows = cur.fetchall()
        brPrijava = podaci[6]
        curr= con.cursor()
        curr.execute("UPDATE user SET login_count = ? WHERE id=?;", (brPrijava+1, podaci[0]))
        con.commit()
        con.close()
    
print("Dobrodosli u Unidu sustav")
print("Za prijavu upišite broj 1, a za registraciju broj 2")
broj = int(input("Unesite broj:"))
while broj!=1 and broj!=2:
    broj = int(input("Unesite broj:"))
if broj==1:
    email = input("Unesite email:")
    lozinka = input("Unesite lozinku:")
    login(email, lozinka)
else:
    email = input("Unesite email:")
    lozinka = input("Unesite lozinku:")
    register_user(email,lozinka)
    
