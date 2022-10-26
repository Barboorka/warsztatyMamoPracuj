# Przelicz stopnie Celsjusza na stopnie Kelvina.
# Użyj funkcji input(), int() i print().

stopnie_C = input('Podaj temperaturę w stopniach Celsjusza:')
przelicznik = 273
stopnie_K = int(stopnie_C) + przelicznik
print(stopnie_C, 'stopni Celsjusza to', stopnie_K, 'stopni Kelvia')
print(f"{stopnie_C} stopni Celsjusza to {stopnie_K} stopni Kelvina.")