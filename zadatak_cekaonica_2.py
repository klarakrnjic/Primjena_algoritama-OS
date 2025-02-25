N, M = map(int, input().split())
zauzeto = set(map(int, input().split()))  # Koristimo set radi bržeg pretraživanja

najbolje_mjesto = None 
najmanja_udaljenost = -1 
udaljenost_rub = 101 

for mjesto in range(1, N + 1):
    if mjesto in zauzeto:
        continue
    
    # Udaljenost do najbližeg zauzetog mjesta
    if zauzeto:
        udaljenost_osoba = min(abs(mjesto - occ) for occ in zauzeto)
    else:
        udaljenost_osoba = N  # Ako nema zauzetih mjesta, bilo koje mjesto je maksimalno slobodno

    # Udaljenost do najbližeg ruba (lijevog ili desnog)
    udaljenost_rub = min(mjesto - 1, N - mjesto)

    # Najbolje mjesto
    if (udaljenost_osoba > najmanja_udaljenost or 
        (udaljenost_osoba == najmanja_udaljenost and udaljenost_rub < udaljenost_rub)):
        najmanja_udaljenost = udaljenost_osoba
        udaljenost_rub = udaljenost_rub
        najbolje_mjesto = mjesto

print(najbolje_mjesto)