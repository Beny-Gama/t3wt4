'''
Faça um progrmra que leia nome e média
ade um aluno, quardando também a situação
em um dicionario. No final, mostre o
conteúdo da estrutura na tela.
'''

aluno = dict()
aluno['nome'] = str(input('None: '))
aluno['média'] = float(input('Média: '))
if aluno['média'] >= 7:
    aluno["situação"] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno["situação"] = 'Recuperação'
else:
    aluno["situação"] = 'Reprovado'
print('-=' * 20)
for k, v in aluno.items():
    print(f'  - {k} é iqual a {v}')