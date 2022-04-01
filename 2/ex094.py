'''
nome sexo idade
a) soma de pesosas
b) média de idade
c) muller cadastradas
d) Lista das pessoas que estão acima da media
'''

galera = list()
pessoa = dict()
soma = cont = 0
while True:
    pessoa.clear()
    pessoa['nome'] = (str(input('Nome: ')))
    while True:
        pessoa['sexo'] = str(input('Sexo [F/M]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por Favor, digite apenas F ou M.')
    pessoa['idade'] = int(input('idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    resp = '-1'
    while True:
        resp = str(input('Quer Continuar [S/N]:')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Por Favor, digite apenas S ou N.')
    if resp in 'N':
        break

print(f'foram  um total de: {len(galera)} pessoas.')

print(f'A média de idade foi de {soma / len(galera)} anos.')

print('O as mulheres cadasgras froma:', end=' ')
for c in galera:
    if c['sexo'] == 'F':
        print(c['sexo'], end=', ')

print('Lista das pessoas com idade que estão acima da media')
for i in galera:
    if i['idade'] > soma / len(galera):
        print(f'    nome = {i["nome"]}; sexo = {i["sexo"]}; idade = {i["idade"]}')
