'''
aprimore o desafio anteiror, mostrando
no final:
A) A soma de todos os valores pares
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
'''
dado = list()
lista = list()

for coluna in range(0, 3):
    dado.clear()
    for linha in range(0, 3):
        dado.append(int(input(f'Numero: [{coluna}][{linha}] ')))
    lista.append(dado[:])

for c in range(0, 3):
    print()
    for i in range(0, 3):
        print(f'[ {lista[c][i]} ]', end='')

'''
print(f'[ {lista[0][0]} ] [ {lista[0][1]} ] [ {lista[0][2]} ]')
print(f'[ {lista[1][0]} ] [ {lista[1][1]} ] [ {lista[1][2]} ]')
print(f'[ {lista[2][0]} ] [ {lista[2][1]} ] [ {lista[2][2]} ]')
'''
print('\n', '-=' * 20)

soma = 0
for n in lista:
    for c in n:
        if c % 2 == 0:
            soma += c
print(f'A soma dos valores pares: {soma}')

somac = 0
for n in lista[2]:
    somac += n
print(f'A soma da terceira coluna: {somac}')

somal = 0
for n in lista:
    somal += n[1]
print(f'A soma da segunda linha: {somal}')
