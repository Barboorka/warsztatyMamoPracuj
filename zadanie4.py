# Przelicz podaną liczbę złotówek na euro.
# Pobierz kwotę za pomocą funkcji input(). Do zamiany typów użyj funkcji float().
# Wyświetl wynik za pomocą funkcji print().
# Przyjmij, że 1 zł = 4.77 euro.

zloty = input('Podaj kwotę w złotówkach: ')
euro = float(zloty) * 4.77
print(f'{zloty} złotych to {euro} euro.')