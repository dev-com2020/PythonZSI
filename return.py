def suma(a,b):
    return a + b

print(suma(2,3))

def kobieta(a):
    if ((a == 'K') or (a == 'k')):
        return "t"
    else:
        return "n"
test = input("Czy jesteś kobietą?[wpisz K lub M]")
if kobieta(test)=="t":
    print('KOBIETA')
else:
    print('MĘŻCZYZNA')
