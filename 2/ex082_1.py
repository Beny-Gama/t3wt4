'''
Crie um programa que cai lei valores númericos e
calcule em uma lista. Depois disso, crie duas lista
extras que vão conter apenas os valores pares
e os valores inpares digitados, respectivamente. ao
fimal, mostre o conteúdo das três lista geradas.
'''

lista = list()
par = list()
impar = list()

while True:
    c = int(input('valor: '))
    lista.append(c)
    resp = '5'
    while resp not in 'NnSs':
        resp = str(input('Quer Continutar: [S/N] ')).strip()[0]
    if resp in 'Nn':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)

print(f'Todos os Valores: {lista}')
print(f'Todos os Pares:   {par}')
print(f'Todos os Impares: {impar}')


