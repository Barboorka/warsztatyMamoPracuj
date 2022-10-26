# czas = 10
# while czas > 0:
#     print(f'Start rakiety za: {czas} sekund.')
#     czas -= 1
# if czas == 0:
#     print('Rakieta wystartowała!')

liczba_poczatkowa = input('Podaj liczbę początkową: ')
liczba_koncowa = input('Podaj liczbę końcową: ')
liczba_poczatkowa = int(liczba_poczatkowa)
liczba_koncowa = int(liczba_koncowa)

while liczba_poczatkowa != liczba_koncowa:
    print(f'Kolejna liczba z podanego przedziału to: {liczba_poczatkowa + 1} ')
    liczba_poczatkowa +=1
if liczba_poczatkowa == liczba_koncowa:
    print('Koniec.')