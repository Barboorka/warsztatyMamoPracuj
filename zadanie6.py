# Używając instrukcji warunkowej if, elif, else przelicz złotówki na wskazaną przez użytkownika walutę.
# Użyj dodatkowo funkcji float(), input(), print() i zapisu do zmiennych.
# Przyjmij, że: 1 euro = 4.77zł, 1 dolar = 4.85zł, 1 forint = 0.011zł.

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