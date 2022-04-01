'''
Faça um prgrama que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
a) Quantas pessoas foram cadastradas.
b) Uma listagem com as pessoas mais pesadas.
c) Uma Listagem com as pessoas mais leves.
'''
mai = men = 0
dado = list()
galera = []

while True:
    resp = '1'
    dado.clear()
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Peso: ')))
    if len(galera) == 0:
        mai = men = dado[1]
    else:
        if dado[1] > mai:
            mai = dado[1]
        if dado[1] < men:
            men = dado[1]
    galera.append(dado[:])
    while resp not in 'SsNn':
        resp = str(input('Quer Continuar [S/N]: ')).strip()[0]
    if resp in 'Nn':
        break

print(f'{len(galera)} pessoas foram cadastradas')
print(f'O Maior peso foi de {mai}Kg', end='')
for p in galera:
    if p[1] == mai:
        print(p[0], end='')
print(f'O Menor peso foi de {men}Kg', end='')
for p in galera:
    if p[1] == men:
        print(p[0], end='')
