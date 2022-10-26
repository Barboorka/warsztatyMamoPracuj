# liczba_km = input('Podaj liczbę kilomtrów: ')
# liczba_km = int(liczba_km)
# jednostka = input('Podaj jednostkę, na którą mam przeliczyć podane wcześniej kilometry (do wyboru: m, cm lub mm): ')
#
# if jednostka == "m":
#     print(f'{liczba_km} kilometrów to {liczba_km * 1000} metrów.')
# elif jednostka == "cm":
#     print(f'{liczba_km} kilometrów to {liczba_km * 10000} centymetrów.')
# elif jednostka == "mm":
#     print(f'{liczba_km} kilometrów to {liczba_km * 1000000} milimetrów.')
# else:
#     print(f'Nasz program nie obsługuje jednostki: {jednostka}.')

zloty = input('Podaj liczbę złotówek: ')
zloty = float(zloty)
waluta = input('Podaj walutę, na którą mam przeliczyć podane wcześniej złotówki (do wyboru: euro, dolar, forint): ')

if waluta == "euro":
    print(f'{zloty} złotych to {zloty * 4.77} euro.')
elif waluta == "dolar":
    print(f'{zloty} złotych to {zloty * 4.85} dolarów.')
elif waluta == "forint":
    print(f'{zloty} złotych to {zloty * 0.011} forintów.')
else:
    print(f'Nasz program nie obsługuje waluty: {waluta}.')