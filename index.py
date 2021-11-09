import sqlite3
from hashlib import blake2b
con = sqlite3.connect('baza.db')

def register_user(email, lozinka):
    cur = con.cursor()
    
    h = blake2b()
    transbyte = str.encode(lozinka)
    h.update(transbyte)
    #ovo je lozinka
    
    vraca = cur.execute("INSERT INTO user (email, password) VALUES (?, ?);", (email, h.hexdigest()))
    if(vraca==True):
        print("Uspjesna registracija")
        print(vraca)
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
    print("Uspjesna prijava")
else:
    email = input("Unesite email:")
    lozinka = input("Unesite lozinku:")
    register_user(email,lozinka)
    
