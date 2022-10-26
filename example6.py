# Przelicz kilometry na wskazaną przez użytkownika jednostkę: metry, centymetry lub milimetry.
# Użyj instrukcji warunkowej if, elif, else oraz funkcji input(), print() i int().

liczba_km = input('Podaj liczbę kilomtrów: ')
liczba_km = int(liczba_km)
jednostka = input('Podaj jednostkę, na którą mam przeliczyć podane wcześniej kilometry (do wyboru: m, cm lub mm): ')

if jednostka == "m":
    print(f'{liczba_km} kilometrów to {liczba_km * 1000} metrów.')
elif jednostka == "cm":
    print(f'{liczba_km} kilometrów to {liczba_km * 10000} centymetrów.')
elif jednostka == "mm":
    print(f'{liczba_km} kilometrów to {liczba_km * 1000000} milimetrów.')
else:
    print(f'Nasz program nie obsługuje jednostki: {jednostka}.')