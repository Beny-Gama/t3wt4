'''
Crie um programa que leia nome e duas
nitas de vários alunos e quarde tido em
em uma lista composta. No final, mostre
um boletim contendo a médio de cada um e
permita que o usuário possa mostrar as notas
de cada aluno individualmente.
'''
lista = list()
dado = list()
ind = list()

while True:
    dado.append(str(input('Nome: ')))
    ind.append(dado[:])
    dado.clear()
    dado.append(float(input('Nota 1: ')))
    dado.append(float(input('Nota 2: ')))
    ind.append(dado[:])
    lista.append(ind[:])
    dado.clear()
    ind.clear()

    resp = '1'
    while resp not in 'SsNn':
        resp = str(input('Quer contunuar [S/N]: ')).strip()[0]
    if resp in 'Nn':
        break

print('-=' * 50)
print('No. NOME', ' ' * 13, 'MÉDIA')
print('-' * 30)

cont = 0
from statistics import mean

for aluno in lista:
    cont += 1
    print(cont, end='  ')
    for separa in aluno:
        if len(separa) % 2 == 1:
            print(separa, ' ' * 10, end='')
        else:
            print(mean(separa))

while resp != 999:
    resp = int(input('Mostrar nota do aluno? [999 interrompe]: '))
    cont = 0
    for aluno in lista:
        cont += 1
        if resp == cont:
            print(aluno)
