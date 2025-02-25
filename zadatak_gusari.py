# Ulazni podaci
N = int(input("Unesi početni broj dragulja: "))

# Izračunavanje broja dragulja za svakog gusara
prvi = N // 4
N -= prvi
drugi = N // 4
N -= drugi
treći = N // 4
N -= treći
četvrti = N // 4

# Ispis rezultata
print(prvi)
print(drugi)
print(treći)
print(četvrti)
