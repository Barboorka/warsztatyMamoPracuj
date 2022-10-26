# Za pomocą funkcji input() i int() pobierz dwie wartości liczbowe: początkową i końcową.
# Użyj pętli while, aby wypisać wszystkie liczby z podanego wyżej przedziału.

liczba_poczatkowa = input('Podaj liczbę początkową: ')
liczba_koncowa = input('Podaj liczbę końcową: ')
liczba_poczatkowa = int(liczba_poczatkowa)
liczba_koncowa = int(liczba_koncowa)

while liczba_poczatkowa != liczba_koncowa:
    print(f'Kolejna liczba z podanego przedziału to: {liczba_poczatkowa} ')
    liczba_poczatkowa +=1
if liczba_poczatkowa == liczba_koncowa:
    print(f'Ostatnia liczba to {liczba_koncowa}. Koniec!')