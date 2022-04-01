'''
Crie um programa que simule o funcionamento
de um caixa eletronico. no inicino, pergunte
ao usuário qual será o valor a ser sacado
(número interio) e o programa vai informar
quantos cédulas de cada valor serão entregues.
OBS: considere que o caixa possui células de
R$50, R$20, R$10 e R$1
'''
from math import floor
print('='*20)
print('{:^20}'.format('Banco Guanabara'))
print('='*20)

while True:
    n = float(input('Qunato você quer sacar? '))
    if n >= 100:
        n100 = floor(n / 100)
        n %= 100
    if n >= 50:
        n50 = floor(n / 50)
        n %= 50
    else:
        n50 = 0
    if n >= 20:
        n20 = floor(n / 20)
        n %= 20
    else:
        n20 = 0
    if n >= 10:
        n10 = floor(n / 10)
        n %= 10
    else:
        n10 = 0
    if n >= 1:
        n1 = floor(n / 1)
    else:
        n1 = 0
    print(
f'''{n100} notas de 100 reais.
{n50} notas de 50 reais.
{n20} notas de 20 reais.
{n10} notas de 10 reais.
{n1} notas d e 1 real.
    ''')
    v = ''
    if v != 'S' and v != 'N':
        v = str(input('Quer Continuar? [S/N] ')).strip().upper()[0]
        if v == 'N':
            break
