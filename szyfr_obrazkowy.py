from turtle import *


def prostokat(a, b, kierunek):
    if kierunek == 'dol':
        fd(a)
        lt(180)
    for i in range(2):
        fd(a)
        lt(90)
        fd(b)
        lt(90)
    if kierunek == 'dol':
        lt(180)
    else:
        fd(a)


def szyfr(alfabet, slowo):
    samogloski = ['a', 'e', 'i', 'o', 'u', 'y']
    for i in range(len(slowo)):
        if slowo[i] in samogloski:
            prostokat(10 * (i + 1), 10 * (alfabet.index(slowo[i]) + 1), 'dol')
        else:
            prostokat(10 * (i + 1), 10 * (alfabet.index(slowo[i]) + 1), 'gora')

szyfr('abcdefghijklmno','lajkonik')
