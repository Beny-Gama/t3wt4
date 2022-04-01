'''
Crie um programa que leia:
a) Todos os valores
b) Todos os pares
c) Todos os impares
'''
lista = list()
par = list()
impar = list()
while True:
    c = int(input('valor: '))
    lista.append(c)
    if c % 2 == 0:
        par.append(c)
    else:
        impar.append(c)
    resp = '5'
    while resp not in 'NnSs':
        resp = str(input('Quer Continutar: [S/N] ')).strip()[0]
    if resp in 'Nn':
        break
print(f'todos os Valores: {lista}')
print(f'Todos os Pares:   {par}')
print(f'Todos os Impares: {impar}')
