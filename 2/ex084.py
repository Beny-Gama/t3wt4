'''
Faça um prgrama que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
a) Quantas pessoas foram cadastradas.
b) Uma listagem com as pessoas mais pesadas.
c) Uma Listagem com as pessoas mais leves.
'''
cont = 0
dado = list()
galera = []
lista = list()
while True:
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Peso: ')))
    galera.append(dado[:])
    resp = '1'
    while resp not in 'SsNn':
        resp = str(input('Quer Continuar: [S/N] ')).strip()[0]
    if resp in 'Nn':
        break
    dado.clear()
print('Pessoas obeses: ', end='')
for c in galera:
    if c[1] >= 80:
        print(c[0], end='...')
print('\n Pessoas Magras: ', end='')
for c in galera:
    if c[1] < 80:
        print(c[0], end='...')

