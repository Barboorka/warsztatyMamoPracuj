#Policz, ile zapłacisz za podaną liczbę kilogramów dyni.
# Pobierz liczbę kilogramów za pomocą funkcji input().
# Przyjmij, że cena dyni wynosi 5 zł/kg.
# Pamiętaj, że liczba kilogramów musi być większa od 0.

liczba_kg = input('Podaj, ile kg dyni chcesz kupić: ')
liczba_kg = float(liczba_kg)
if liczba_kg > 0:
    cena = liczba_kg * 5
    print(f'{liczba_kg} kilogramów dyni kosztuje {cena} złotych.')
else:
    print(f'Waga dyni nie może być mniejsza od 0. Podano: {liczba_kg}')

cena_dyni = 5
liczba_kg = input('Podaj, ile kg dyni chcesz kupić: ')
liczba_kg = float(liczba_kg)
if liczba_kg > 0:
    koszt = liczba_kg * cena_dyni
    print(f'{liczba_kg} kilogramów dyni kosztuje {koszt} złotych.')
else:
    print(f'Waga dyni nie może być mniejsza od 0. Podano: {liczba_kg}')