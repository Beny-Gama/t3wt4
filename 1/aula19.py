# VARIÁVEIS COMPOSTAS (DICIONAIROS)

pessoas = {'nome': 'Gustava', 'sexo': 'M', 'idade': 22}
print(pessoas)
print(pessoas['nome'])
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print('-='*20)
for k in pessoas.keys():
    print(k)
print('-='*20)
for v in pessoas.values():
    print(v)
print('-='*20)
for item, valor in pessoas.items():
    print(f'{item} = {valor}')
print('-='*20)
del pessoas['sexo']
print(pessoas)
print('-='*20)
pessoas['nome'] = 'Leandro'
print(pessoas)
print('-='*20)
pessoas['peso'] = 98.5
print(pessoas)
print('-='*20)

'''
brasil = list()
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(estado1)
print(estado2)
print(brasil)
print(brasil[0])
print(brasil[1])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])
'''
'''
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Únidade Federativa: '))
    estado['sigle'] = str(input('Sigla do Estado: '))
    # brasil.append(estado[:]) # fatiamendo utilizando [:] não funciona com dicionairos.
    brasil.append(estado.copy()) # O fatiamendo em dicionairos é utilizado com metodo interno .copy()
print(brasil)
for e in brasil:
    print(e)
print('-=' * 20)
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')
print('-=' * 20)
for e in brasil:
    for v in e.values():
        print(v)
print('-=' * 20)
for e in brasil:
    for v in e.values():
        print(v, end=' ')
        print()
'''