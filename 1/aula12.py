'CONDIÇÕES ANINHADAS'

"""
ex1:
if carro.esquerda():
alif carro.direira():
alse:

ex2:
if carro.esquerda():
alif carro.direira():
alif carro.ré():
alse:

ps: pode usar quantas "alif" nessesarios.
"""

n = str(input('Qual é seu nome? ')).strip()
nome = n.lower().title()
if nome == 'Bernardo':
    print('Que nome Bonito {}!'.format(nome))
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem polular no Brasil {}.'.format(nome))
elif nome == 'Maria' or nome == 'Joana' or nome == 'Carla':
    print('Belo nome Feminino {}!'.format(nome))
else:
    print('Tenha um bom dia {}!'.format(nome))
