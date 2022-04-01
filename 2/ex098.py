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

def pri():
    print()
    print('~' * 20)


for c in range(1, 10 + 1):
    sleep(.3)
    print(f'{c} ', end='')

pri()

for c in range(10, 0, -2):
    sleep(.3)
    print(f'{c} ', end='')

pri()

print('Agora é sua fez de persolalizar a contagem.')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passos: '))

if ini < fim:
    if pas > 0:
        for c in range(ini, fim + 1, pas):
            sleep(.3)
            print(f'{c} ', end='')
    elif pas < 0:
        for c in range(fim, ini - 1, pas):
            sleep(.3)
            print(f'{c} ', end='')

if ini > fim:
    if pas > 0:
        for c in range(fim, ini - 1, - pas):
            sleep(.3)
            print(f'{c} ', end='')

    elif pas < 0:
        for c in range(fim, ini - 1, pas):
            sleep(.3)
            print(f'{c} ', end='')