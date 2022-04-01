'''
Crie um programa que leia
'''
from datetime import datetime
dicio = dict()

dicio['nome'] = str(input('Nome: '))
nasc = int(input('Data de Nascimento: '))
dicio['idade'] = datetime.now().year - nasc
dicio['Carteira de Trabalho'] = int(input('Carteira de Trabalho (0 não tem): '))
if dicio['Carteira de Trabalho'] != 0:
    nasc = int(input('Ano de Contrimuição: '))
    dicio['anos contratação'] = dicio['idade'] + (nasc + 35) - datetime.now().year
    dicio['Sala'] = float(input('Salario: '))

for k, i in dicio.items():
    print(f'{k} tem o valor {i}')