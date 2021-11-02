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
    print("Uspjesna registracija")
    
