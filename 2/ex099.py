'''
Faça um programa que tenha uma função
chamada maior(), que receba vários
parâmetros com valores interiros.

Seu programa tem que analizar todos os valores
e dizer qual deles é o maior.
'''

from time import sleep


def maior(* num):
    print("-=" * 30)
    print('Analizando os Valores Passaos... ')
    sleep(1)
    m = 0
    for c in num:
        sleep(0.3)
        print(c, end=' ')
        if c > m:
            m = c
        sleep(0.3)
    print(f'Foram {len(num)} valores ao todo.')
    print(f'O maior valor imformado é {m}.')


maior(2, 9, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
