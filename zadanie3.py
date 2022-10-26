# Przelicz kilometry na metry.
# Pobierz liczbę kilometrów za pomocą funkcji input().
# Do zamiany typów użyj funkcji int().
# Wyświetl wynik za pomocą funkcji print().

liczba_km = input('Podaj liczbę kilometrów: ')
liczba_m = int(liczba_km) * 1000
print(f'{liczba_km} kilometrów to {liczba_m} metrów.')