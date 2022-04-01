'''
Desenvolva um programa que leia
quatro valores pelo teclado e
quarde-os em uma tupla. no final,
mostre:
A) Quantas vezes aparecei o valor 9
B) Em que posição foi digitado o primeiro valor
C) Quais foram os números pares.
'''
n = (int(input('Digite um numero: [1, 10] ')),
     int(input('Digite outro numero: [1, 10] ')),
     int(input('Digite mais um numero: [1, 10] ')),
     int(input('Digite o último número: [1, 10] ')))

print('os valore digitados foram: {}'.format(n))
print(f'O valor 9 apareceu: {n.count(9)} vezes')
if 3 in n:
    print(f'O valor 3 apareceu: {n.index(3)+1}ª posição')
print(f'Os valores pares digitados foram: ', end='')
for i in n:
    if i % 2 == 0:
        print(i)
