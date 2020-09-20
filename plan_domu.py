import turtle

# współrzędne ścian (poczatek_x, poczatek_y, koniec_x, koniec_y)

mieszkanie = [
    # kuchnia
    (0, 0, 100, 0),
    (0, 0, 0, 100),
    (0, 100, 100, 100),

    # kuchnia - drzwi do korytarza
    (100, 100, 100, 80),
    (100, 0, 100, 40),

    # korytarz - drzwi wyjsciowe
    (100, 0, 120, 0),
    (160, 0, 180, 0),

    # korytarz
    (180, 0, 180, 100),

    # korytarz - drzwi do pokoju
    (180, 100, 160, 100),
    (100, 100, 120, 100),

    # pokoj
    (0, 100, 0, 200),
    (0, 200, 180, 200),
    (180, 200, 180, 100),
]

# kolory ścian

colors = [
    "#880000", "#884400", "#888800", "#008800",
    "#008888", "#000088", "#440088", "#880088"
]

colors_count = len(colors)
selected_colors = 0

# grubość ścian
turtle.width(5)

# rysowanie kolejnych ścian różnymi kolorami

for sciana in mieszkanie:

    # współrzędne końców ściany

    x1, y1, x2, y2 = sciana

    # ustawienie koloru

    turtle.color(colors[selected_colors])

    # przesuniecie do początku - bez rysowania

    turtle.penup()
    turtle.setpos(x1, y1)

    # przesuniecie do końca - z rysowaniem

    turtle.pendown()
    turtle.setpos(x2, y2)

    # kolejny kolor 'modulo' ilość kolorów

    selected_colors = (selected_colors + 1) % colors_count

# schowanie żółwika

turtle.hideturtle()

# obsługa zdarzeń (aby dało się zamknąć okienko)

turtle.mainloop()
