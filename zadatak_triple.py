# Ulazni podaci
P = int(input("Unesi broj poena: "))
S = int(input("Unesi broj skokova: "))
A = int(input("Unesi broj asistencija: "))

# Provjera uvjeta za triple-double
if P >= 10 and S >= 10 and A >= 10:
    print("DA")
    print(max(P, S, A))  # Najveća vrijednost
else:
    print("NE")
    print(min(P, S, A))  # Najmanja vrijednost