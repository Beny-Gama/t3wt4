'''
Faça um programa que tenha ima lista
chamada números e duas funções chamadas
sorteia() e somaPar(). A Primeiro função
vai sortear 5 números e vai colocá-los
dentro da lista e a seunga função vai mostrar
a soma entre todos ps valores PARES sorteados
pela dincáo anteiror.
'''
lst = list()

def sorteia(quantidade, inicio, fim):
    from random import randint
    from time import sleep

    print(f'Sorteando {quantidade} valores da lista: ', end='')
    for c in range(0, quantidade):
        n = randint(inicio, fim)
        lst.append(n)
        print(n, end=' ')
        sleep(.3)
    print(f'\nOs valores sorteados {lst}')


def somaPar(): #Soma Valor par de uma lista
    soma = 0
    for c in lst:
        if c % 2 == 0:
            soma += c
    print(f'A soma dos valores pares é {soma}')


sorteia(5, 1, 50)
somaPar()
