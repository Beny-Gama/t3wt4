"LAÇOS DE REPETIÇÃO [PARTE 2]"
"ESTRUTURA DE REPETÇÃO COM TESTE LOGICO"

'''
enquanto não [maça]
    passo
pega
while not [maça]
    passo
pega


enquanto não maça
    se ploco
        passo
    se vazio
        pula
    se moeda
        pega
pega

while not maça
    if ploco
        passo
    if vazio
        pulo
    if moeda
        pega
'''

'''c = 1
while c < 10:
    print(c)
    c += 1
print('Fim')'''

'''for c in range(1, 5):
    n = int(input('Digite um Valor: '))
print('fim')'''

'''
r = 'S'
while r == "S":
    n = int(input('Digite um Valor: '))
    r = str(input('Quer Continuar? [S/N]: ')).upper()
print('fim')
'''

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um Valor: '))
    if n != 0:
        if n % 2 == 0:
             par += 1
        else:
            impar += 1
print('''Pares: {} 
Imares: {}'''.format(par, impar))
