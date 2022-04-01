'''
Crie uma tupla preenchida com 20 primeiros
colocados da tabela do brazileirão,
na ordem de colocação. depois
mostre.
a) apenas os 5 primeros colocados
b) os ultimos 4 colocado
c) a lista dos times em ordem alfaberica
d) Em que posição na tabela está a 'chapecoence'
'''

t = ('Alélico-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino',
'Fluminense', 'América-MG', 'Atlético-GO', 'Santos', 'Ceará SC', 'Interacional',
'São Paulo', 'Atlético-PR', 'Cuiabá', 'Juventude', 'Grêmio', 'Bahia',
'Sport Recife', 'Chapecoense')
print(f'Os 5 primeiros colocados são: {t[:5]}')
print(f'Os 4 últimos colocados são: {t[-4:]}')
print(f'Em ordem alfabética é: {sorted(t)}')
print(f"Chapecoense está na {t.index('Chapecoense') + 1}ª posição")