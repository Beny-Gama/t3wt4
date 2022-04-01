'''Curso Python #16 - Tuplas'''
'''lanche = ('Hambúrquer','Suco', 'pizza', 'pudim')
print(lanche[:2])'''

# Tuplas são imutaveis!!!
'''lanche = ('Hambúrquer','Suco', 'pizza', 'pudim')
lanche[1] = 'Refrigerante'
print(lanche)'''


lanche = ('Hambúrquer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

'''for comida in lanche:
    print(f"Ele quer comer: {comida}")'''

'''for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')'''

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')


'''lanche = ('Hambúrquer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

print(sorted(lanche))
print(lanche)'''


'''a = (2, 5, 4)
b = (5, 8, 1, 2, 8)
c1 = a + b
c2 = b + a
print(c1)
print(c2)

print('Qunatos', c1.count(2)) #Conta na Tutla
print('Onde', c1.index(8)) #Prcura na Tupla'''

'''# Tuplas são deletaveis
pessoa = ('Gustavo', 39, 'M', 99.88)
del(pessoa)
print(pessoa)
'''