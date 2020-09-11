try:
    print('*** dzielenie ***')
    a = int(input('Podaj pierwszą liczbę: '))
    b = int(input('Podaj drugą liczbę: '))
    print(a/b)
except ValueError:
    print('błąd, nie podałeś prawidłowej liczby!')
except ZeroDivisionError:
    print('błąd, nie mogę podzielić przez 0!')
