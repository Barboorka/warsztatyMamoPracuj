# Napisz program, który wykona odliczanie od 10 do 0.
#
czas = 10
while czas > 0:
    print(f'Start rakiety za: {czas} sekund.')
    czas -= 1
if czas == 0:
    print('Rakieta wystartowała!')