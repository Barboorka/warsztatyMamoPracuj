# Przelicz stopnie Celsjusza na stopnie Kelvina.
# Pobierz liczbę stopni Celsjusza za pomocą funkcji input().
# Sprawdź, czy podana wartość jest większa lub równa -273.

stopnie_C = input('Podaj temperaturę w stopniach Celsjusza: ')
stopnie_C = int(stopnie_C)
if stopnie_C>= -273:
    stopnie_K = stopnie_C + 273
    print(f'{stopnie_C} stopni Celsjusza to {stopnie_K} stopni Kelvina.')
else:
    print(f'Temperatura w stopniach Celsjusza nie może być mniejsza niż -273. Podano: {stopnie_C}')