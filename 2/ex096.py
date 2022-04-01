'''
Faça um programa que tenha uma função
chamada área(), que receba as dimesões de
um terreno restangular( largura e comprimento)
e mostre a área do terreno.
'''

def area(a, b):
    c = a * b
    print(f'A area de um terreno {a}x{b} é de {c}m²')


larg = float(input('Largura (m): '))
comp = float(input('Comprimento (m): '))
area(larg, comp)
