'''
Crie um programa que crie uma
matriz de dimenção 3x3 e preencha
com valores lidos pelo teclado.
Ex:
[ ] [ ] [ ]
[ ] [ ] [ ]
[ ] [ ] [ ]
No fonal, mostre a matriz na tela,
com a promatação correta.
'''
lista = list()
dados = list()

for c in range(0, 3):
    dados.append(int(input(f'Valor: [0][{c}] ')))
lista.append(dados[:])
dados.clear()
for c in range(0, 3):
    dados.append(int(input(f'Valor: [1][{c}] ')))
lista.append(dados[:])
dados.clear()
for c in range(0, 3):
    dados.append(int(input(f'Valor: [2][{c}] ')))
lista.append(dados[:])

print(lista)
print(f'[ {lista[0][0]} ] [ {lista[0][1]} ] [ {lista[0][2]} ]')
print(f'[ {lista[1][0]} ] [ {lista[1][1]} ] [ {lista[1][2]} ]')
print(f'[ {lista[2][0]} ] [ {lista[2][1]} ] [ {lista[2][2]} ]')
