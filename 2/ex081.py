'''
Crie um programa que vai ler vários
números lista. depois disso, mostre:
A) Quantos números forom digotodos.
B) A lista de valores, ordenados de foram decresente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''
lista = list()
resp = ''
while True:
    lista.append(int(input('Valor: ')))
    resp = '-1'
    while resp not in "SsNn":
        resp = str(input('Gosria de parar: [N/S] ')).strip()[0]
    if resp in "Nn":
        break
print(f'Você digitou {len(lista)} valores.')
lista.sort(reverse=True)
print(f'Na ordem deresente fica:', lista)
if 5 in lista:
    print(f'Você digitou 5: {lista.count(5)} vezes.')
else:
    print('Não tem 5 na lista.')
