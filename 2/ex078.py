'''
Escreva um programa que leia 5 valores
numericos e quande-os em uma lista.
No final, mostrre qual foi o maior e o menor
valor digitados e as suas respectivas posilções
na lista.
'''
lista = []
for c in range(0, 5):
    lista.append(int(input(f'{c}º Valor: ')))
print(f'\nO MAIOR valor é {max(lista)} Nas Posições: ', end='')
for i, v in enumerate(lista):
    if v == max(lista):
        print(i, end=' ')
print(f'\nO MENOR valor é {min(lista)} Nas Posições: ', end='')
for i, v in enumerate(lista):
    if v == min(lista):
        print(i, end=' ')
