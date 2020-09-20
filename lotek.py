import #uzupełnij import

try:
    ileliczb = int(input("Podaj ilość typowanych liczb: "))
    maksliczba = int(input("Podaj maksymalną losowaną liczbę: "))
    if ileliczb  maksliczba: #uzupełnij odpowiedni znak porównania
        print("Błędne dane!")
        exit()
except ValueError:
    print("Błędne dane!")
    exit()

liczby = []
i = 0
while i < ileliczb:
    liczba = random.randint(1, maksliczba)
    if liczby.count(liczba) == 0:
        liczby.(liczba)	# uzupełnij metodę
        i = # uzupełnij kod

for i in range(3):
    print("Wytypuj %s z %s liczb: " % (ileliczb, maksliczba))
    typy = set()
    i = 0
    while i < ileliczb:
        try:
            typ = int(input("Podaj liczbę %s: " % (i + 1)))
        except ValueError:
            ("Błędne dane!") #uzupełnij linie kodu
            continue

        if 0 < typ <= maksliczba and typ not in typy:
            typy.add(typ)
            i = i + 1

    trafione = set(liczby) & typy
    if trafione:
        print("\nIlość trafień: %s" % len(trafione))
        print("Trafione liczby: ", trafione)
    else:
        print("Brak trafień. Spróbuj jeszcze raz!")

    print("\n" + "x" * 40 + "\n")  

print("Wylosowane liczby:", ) # uzupełnij nazwe zmiennej
