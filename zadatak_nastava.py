# U voćnjaku raste nekoliko vrsta voćaka: jabuke, kruške i šljive. Želimo izračunati koliko ukupno plodova imamo u voćnjaku. Prosječno svaka jabuka ima 8 plodova, kruška 6 plodova, a šljiva 10 plodova. Napišite program koji će omogućiti unos broja voćaka u voćnjaku te ispisati koliko ukupno plodova imamo u voćnjaku.

# Ulazni podaci
J = int(input()) # Broj stabala jabuka
K = int(input()) # Broj stabala krušaka
Š = int(input()) # Broj stabala šljiva

# Izračun ukupnog broja stabala
ukupno_plodova = J*8 + K*6 + Š*10

# Ispis rezultata
print(ukupno_plodova)
