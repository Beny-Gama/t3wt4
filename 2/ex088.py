'''
Faça um progrmaa que ajude um jogador
da MEGA SENA a crier palpites. o prograna
vai perguntar quantos jogos serão gerados
e vai sortear 6 números entre 1 e 60 para
cada jogo, cadastrado tudo em uma lista
composta.
'''

from time import sleep
from random import randint
lista = list()
n = int(input('Digite quantos Jogos voce quer? '))

for c in range(0, n):
    sleep(0.5)
    for t in range(0, 6):
        lista.append(randint(1, 60))
        lista.sort()
    print(f'Jogo {c + 1}:', lista)
    lista.clear()
