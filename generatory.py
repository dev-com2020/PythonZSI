#def liczby():
#    for i in range(11):
#        yield i * 2
#for parzysta in liczby():
#    print(parzysta)

def genarator():
    x = 0
    while True:
        y = yield x
        if y is None:
            x = x + 1
        else:
            x = y

g = genarator()
print(next(g))
print('coś innego')
print(next(g))
print(next(g))
print('coś innego')
print(next(g))
print(g.send(12))
print(next(g))
print('coś innego')
print(next(g))

