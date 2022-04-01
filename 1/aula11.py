'CORES'

'''
style
0 = none
1 = bald
4 = underline
7 = negative

text
30 = none
31 = vermelho = red
32 = verde = grem
33 = amarelo = yelow
34 = azul escuro = 
35 = roxo/lilás
36 = azul claro
37 = cinza

back
40 = none
41 = vermelho = red
42 = verde = grem
43 = amarelo = yelow
44 = azul escuro = dark blue
45 = roxo/lilás 
46 = azul claro = what blue
47 = cinza = grey
'''

print('\033[0:30:41mteste')
print('\033[4:33:41mteste')
print('\033[1:35:43mteste')
print('\033[30:42mteste')
print('\033[mteste')
print('\033[7:30mteste')

print('\033[0:30:41mteste\033[m')
print('\033[4:33:41mteste\033[m')
print('\033[1:35:43mteste\033[m')
print('\033[30:42mteste\033[m')
print('\033[mteste\033[m')
print('\033[7:30mteste\033[m')

a = 3
b = 5

print('Os valores \033[32m{}\033[m e \033[34m{}\033[m!!!'.format(a, b))

nome = 'Bernardo'
print('Muito frazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))

cores = {'limpa' : '\033[m',
         'azul' : '\033[34m',
         'amaremlo' : '\033[33m',
         'pretoebranco' : '\033[7;30m'}

print('Muito frazer em te conhecer, {}{}{}!!!'.format(cores['pretoebranco'], nome, cores['limpa']))
