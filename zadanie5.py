# stopnie_C = input('Podaj temperaturę w stopniach Celsjusza: ')
# stopnie_C = int(stopnie_C)
# if stopnie_C>= -273:
#     stopnie_K = stopnie_C + 273
#     print(f'{stopnie_C} stopni Celsjusza to {stopnie_K} stopni Kelvina.')
# else:
#     print(f'Temperatura w stopniach Celsjusza nie może być mniejsza niż -273. Podano: {stopnie_C}')

# liczba_kg = input('Podaj, ile kg dyni chcesz kupić: ')
# liczba_kg = float(liczba_kg)
# if liczba_kg > 0:
#     cena = liczba_kg * 5
#     print(f'{liczba_kg} kilogramów dyni kosztuje {cena} złotych.')
# else:
#     print(f'Waga dyni nie może być mniejsza od 0. Podano: {liczba_kg}')

cena_dyni = 5
liczba_kg = input('Podaj, ile kg dyni chcesz kupić: ')
liczba_kg = int(liczba_kg)
if liczba_kg > 0:
    koszt = liczba_kg * cena_dyni
    print(f'{liczba_kg} kilogramów dyni kosztuje {koszt} złotych.')
else:
    print(f'Waga dyni nie może być mniejsza od 0. Podano: {liczba_kg}')