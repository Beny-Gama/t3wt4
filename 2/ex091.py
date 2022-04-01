'''
Crie um progrma onde 4 jogadores joguem
um dado e tenham resultado aleatórios.
Guarde esses resultados em um dicionario.
No final, coloque esse dicionario em ordem
savendo que o vencedor tirou o maior número
no dado.
'''
from time import sleep
from random import randint
from operator import itemgetter
jogo = dict()
ranking = list()

for c in range(0, 4):
    jogo[f'Jogador{c}'] = randint(1, 6)

for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print()
print(' <<<<<  ranking  >>>>> ')

cont = 0
for k, v in ranking:
    cont += 1
    print(f'{cont} lugar: {k} tirou {v}')
    sleep(1)