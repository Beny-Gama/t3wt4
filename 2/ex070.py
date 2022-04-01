"""
Crie um programa que leia o nome e o
preço de vários produtos. O programa
deverá perguntar se o usuário vai
continuar. No final, mostre:

A = Qual é o total gasto na compra.
B = Quantos proditos custam mais de
R$: 1000.
C = Qual é o nome do produto mais barato
"""
barato = soma = cbarato = c1000 = 0
vbarato = ''
while True:
    v = ''
    nome = str(input('Nome do produto: ')).strip()
    preço = float(input('Preço: '))
    soma += preço
    if barato == 0:
        barato = preço
        vbarato = nome
    else:
        if preço < barato:
            barato = preço
            vbarato = nome
    if preço > 1000:
        c1000 += 1
    while v != 'S' and v != 'N':
        v = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if v == 'N':
        break
print(f'R$:{soma:.2f} foram gastos.')
print(f'{c1000} produtos comprados com mais de 1000 Reais.')
print(f'{vbarato} Foi o produto mais barato, custando R$:{barato:.2f}.')
