N = int(input().strip())
for _ in range(4):
    dragulji = N // 4  # Izračunaj dragulje koje gusar uzima
    print(dragulji)   # Ispiši rezultat
    N -= dragulji     # Ažuriraj preostali broj dragulja za sljedećeg gusara

