'''crie um programa que tenha um tupla
única com nomes de produtos e seus
respectivos preços, na sequência.
No final, mostre uma listagem de precos,
organiando os dados en forma tabular.
'''
lista = ('Macarrão', 2.50, 'Jujuba', 1, 'Frango', 6.99, 'Balão', 1.20,
         'Presunto', 6.40, 'Carvão', 10.50, 'Abacaxi', 5.3)

print('-'*40)
print(f'{"Listagem de Preços":^40}'.upper())
print('-'*40)

for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R$:{lista[pos]:>7.2f}')
