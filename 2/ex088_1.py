from random import randint
cont = 0
lista = list()
while True:
    num = randint(1, 60)
    if num in lista:
        lista.append(num)
        cont += 1
    if cont >= 6:
        break
lista.sort()
print(f'Os numeros sortedos foram {lista}')