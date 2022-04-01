'''
faça um programa que leia 5 valores
numerricos e guarde-os em uma lista.

no final, mostre qual foi maior e o
menor valor digitado e os seus
respectivas posições na lista.
'''

lista = ('Bailarina', 'Futebol', 'Estátua', 'Pintor', 'Frio', 'Bebê', 'Mímico',
'Escova de dentes', 'Lápis', 'Livro', 'Astronauta', 'Amor', 'Ódio', 'Cego',
'Cadeira', 'Sacola', 'Professor', 'Médico', 'Calculadora', 'Artista', 'Vitória',
'Pescador', 'Internet', 'Basquete', 'Semente', 'Policial', 'Amargo', 'Bilhete',
'Xadrez', 'Banana', 'Micróbio', 'Romance', 'Carteira', 'Máquina de lavar',
'Prancha de surfe', 'Debate', 'Lixo', 'Sombra', 'Cadeado', 'Massagem')
for p in lista:
    print(f'\nPalavra: {p} Tem: ', end='')
    for letra in p:
       if letra.lower() in 'aeiouáâãàéêèíîìóôõòúûù':
           print(letra, end='')
