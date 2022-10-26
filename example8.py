# Napisz program sprawdzający prędkość. Pobierz od użytkownika wartość.
# Jeżeli wartość jest mniejsza lub równa 50, wypisz: "Jedziesz przepisowo!".
# Jeżeli wartość jest większa niż 50 i mniejsza niż 80, wypisz: "Za szybko jedziesz! Zwolnij!".
# Jeżeli wartość jest większa niż 50 i mniejsza niż 80, wypisz: "Zdecydowanie za szybko jedziesz! zaraz dostaniesz mandat!"
# Jeżeli wartość jest większa niż 100, wypisz: "Dostajesz mandat!".
# Zakończ działanie programu, jeśli użytkownik wpisze słowo "koniec".

predkosc = input('Podaj prędkość. Jeśli chcesz zakończyć, wpisz słowo koniec.')
while predkosc.lower() != 'koniec':
    print('Sprawdzanie prędkości...')
    predkosc = int(predkosc)
    if predkosc <= 50:
        print('Jedziesz przepisowo!')
    elif predkosc <80:
        print('Za szybko jedziesz! Zwolnij!')
    elif predkosc <100:
        print('Zdecydowanie za szybko jedziesz! zaraz dostaniesz mandat!')
    else:
        print('Dostajesz mandat!')
    predkosc = input('Podaj prędkość. Jeśli chcesz zakończyć, wpisz słowo koniec.')