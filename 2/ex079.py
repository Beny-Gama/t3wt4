'''
Crie um programa onde o usuário possa digitar
vários valores numericos e cadastre-os em uma
lista. Caso o número já exista lá dentro, ele
não será adicionado. no final, serão exibidos
todos os valores únicos digitados em ordem
crescente.
'''
lista = []
while True:
    c = int(input('Valor: '))
    if c in lista:
        lista.pop()
        print('Esse valor já exite! ')
    else:
        lista.append(c)
    v = ''
    while v != 'S' and v != 'N':
        v = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if v == 'N':
        break
print(lista.sort())
