import sqlite3
import random
from hashlib import blake2b
from datetime import datetime
from datetime import timedelta


def register_user(email, lozinka):
    con = sqlite3.connect('baza.db')
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
    con = sqlite3.connect('baza.db')
    cur = con.cursor()
    
    h = blake2b()
    transbyte = str.encode(lozinka)
    h.update(transbyte)
    
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

def provjera(email):
    hashhh=0
    con = sqlite3.connect('baza.db')
    cur = con.cursor()

    cur.execute("SELECT * FROM user WHERE email= ?;", (email,))
    podaci= cur.fetchone()
    idd=podaci[0]
    if podaci[2]==email:
        hashhh=generirajHash(idd)
    else:
        print("Email koji ste unijeli nema aktivan profil")
    con.commit()
    con.close()
    return hashhh

    
    
def generirajHash(idd):
    con = sqlite3.connect('baza.db')
    cur = con.cursor()
    hashh = random.getrandbits(32)
    print(hashh)
    now = datetime.now()
    now_plus_30 = now + timedelta(minutes = 30)
    vrijeme=now_plus_30.strftime("%H:%M:%S")
    print(vrijeme)
    print(idd)
    cur.execute("INSERT INTO forgot_password (id,hash,valid_until) VALUES (?, ?, ?);", (idd, hashh,vrijeme))
    con.commit()
    con.close()
    return hashh

    
    



print("Dobrodosli u Unidu sustav")
print("Za prijavu upišite broj 1, a za registraciju broj 2")
broj = int(input("Unesite broj:"))
while broj!=1 and broj!=2:
    broj = int(input("Unesite broj:"))
if broj==1:
    email = input("Unesite email:")
    lozinka = input("Unesite lozinku(za zaboravljenu lozinku unseite broj 3):")
    if(lozinka=="3"):
        email = input("Unesite email za koji ste zaboravili lozinku:")
        hash1=provjera(email)
        email_promjena = input("Za promjenu lozinke unesite email")
        hash_promjena = input("Za promjenu lozinke unesite hash koji ste dobili")
        print(email)
        print(email_promjena)
        print(hash1)
        print(hash_promjena)
        print(email==email_promjena)
        print(hash_promjena==hash1)
        if(email==email_promjena and hash_promjena==str(hash1)):
            nova_lozinka = input("Unesite novu lozinku")
            potvrda_nove_lozinke = input("Potvrdite novu lozinku")
            if(nova_lozinka==potvrda_nove_lozinke):
                con = sqlite3.connect('baza.db')
                curr = con.cursor()
                h = blake2b()
                transbyte = str.encode(nova_lozinka)
                h.update(transbyte)
                curr.execute("SELECT * FROM user WHERE email= ?;", (email,))
                podaci= curr.fetchone()
                idd=podaci[0]
                curr.execute("UPDATE user SET password = ? WHERE email=?;", (h.hexdigest(), email_promjena))
                curr.execute("DELETE FROM forgot_password WHERE id=?;", (idd,))
                con.commit()
                con.close()
    else:
        login(email, lozinka)
else:
    email = input("Unesite email:")
    lozinka = input("Unesite lozinku:")
    register_user(email,lozinka)
    
