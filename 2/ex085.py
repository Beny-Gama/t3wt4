'''
Crie um ptograma onde o usuário possa
digitar sete valores valores numericos
e cadastre-os em uma lista única que
montehnha separados os valores pares
e ímpares. No final, mostre os valores
pares e ímapres em ordem crescente.
'''
dado = list()
par = list()
impar = list()
for c in range(0, 7):
    dado.append(int(input('Numero: ')))
for e in dado:
    if e % 2 == 0:
        par.append(e)
    else:
        impar.append(e)
par.sort()
impar.sort()
print(f'{par} são pares.')
print(f'{impar} sáo impares.')