import random

def deko(fn):
    def dodaj():
        print('kostka rzucona...')
        print('kostka się zatrzymała na wyniku:')
        fn()
    return dodaj


@deko
def rzut_kostka():
    print(random.randint(1,6))

rzut_kostka()
