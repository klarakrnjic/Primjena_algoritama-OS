N, M = map(int, input().split())
zauzeta = list(map(int, input().split()))

najbolje_mjesto = None
najveća_udaljenost = -1 
najmanja_udaljenost_do_ruba = None

# Provjera svih mjesta od 1 do N
for mjesto in range(1, N + 1):
    if mjesto in zauzeta:
        continue

    # Izračunaj udaljenost do najbliže zauzetog mjesta
    udaljenosti = [abs(mjesto - z) for z in zauzeta]
    udaljenost_do_osobe = min(udaljenosti)
    
    # Izračunaj udaljenost do najbližeg ruba
    udaljenost_do_ruba = min(mjesto - 1, N - mjesto)
    
    # Želimo maksimizirati udaljenost do najbliže zauzete osobe
    if udaljenost_do_osobe > najveća_udaljenost:
        najveća_udaljenost = udaljenost_do_osobe
        najbliže_rubu = udaljenost_do_ruba
        najbolje_mjesto = mjesto

    # Ako su udaljenosti do osobe jednake, koristimo kriterij "bliže rubu"
    elif udaljenost_do_osobe == najveća_udaljenost:
        if najbliže_rubu is None or udaljenost_do_ruba < najbliže_rubu:
            najbliže_rubu = udaljenost_do_ruba
            najbolje_mjesto = mjesto
        elif udaljenost_do_ruba == najbliže_rubu and mjesto < najbolje_mjesto:
            najbolje_mjesto = mjesto

# Ispiši odabranu poziciju
print(najbolje_mjesto)
