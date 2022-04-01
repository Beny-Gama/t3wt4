"LAÇOS DE REPETIÇÃO [PARTE 1]"
"ESTRUTURA DE REPETÇÃO COM VARIAVEL DE CONTROLE"

"""
for c in range(0,3):
    passo
    pula
passo
pega

for c in range(0,3):
    if meda
        pega
    passo
    pula
passo
pega
"""
for c in range(1, 3):
    print('Olá!')
print('fim')

for c in range(6, 0, -1):
    print(c)
print('fim')

for c in range(0, 7, 2):
    print(c)
print('fim')

"""n = int(input('Digite um número '))
for c in range(0, n+1):
    print(c)
print('Fim!')"""

'''i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')'''

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('O Somatorio de todos os valores foi {}'.format(s))
