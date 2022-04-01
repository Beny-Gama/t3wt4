'''
Faça um programa que tenha uma
função chamada contador(), que
receba três paramentros: inicio,
fim e passadp e realize a contagem.

Seu Programa tem que realizar três
contagens através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem persolaizada
'''
from time import sleep


def contator(ini, fim, pas=0):
    print('~' * 20)
    if pas == 0:
        pas = -1
    if ini < fim:
        if pas > 0:
            for c in range(ini, fim + 1, pas):
                sleep(.3)
                print(c, end=' ')
        else:
            for c in range(ini, fim + 1, - pas):
                sleep(.3)
                print(c, end=' ')
    if ini > fim:
        if pas > 0:
            for c in range(ini, fim - 1, - pas):
                print(c, end=' ')
                sleep(.3)
        else:
            for c in range(ini, fim - 1, pas):
                print(c, end=' ')
                sleep(.3)
    print()
    print('~' * 20)


contator(1, 10, 1)
contator(10, 0, 2)

contator(90, 40, 10)
contator(20, 10, -1)
contator(40, 90, -10)
contator(20, 10, 0)

'''
contator(int(input('INICIO: ')),
         int(input('FIM: ')),
         int(input('PASSOS: ')))
'''
