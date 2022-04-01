# Curso Python #20 - Funções (Parte 1)
'''
def lin():
    print('-' * 30)

lin()
print('  CURSO EM VIDEO  ')
lin()
print('  APRENDA PYTHON  ')
lin()
print('  GUSTAVO QUANABARA  ')
lin()
'''

'''
def mensagem(msg):
    print('-' * 30)
    print(f'  {msg}   ')
    print('-' * 30)

mensagem('SISTEMA DE ALUNOS')
mensagem('APRENDA PYTHON')
mensagem('GUSTAVO QUANABARA')
'''
'''
def soma(a, b):
    s = a + b
    print(s)

soma(4, 2)
soma(1, 3)
'''

'''
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(s)


soma(b=4, a=3)
soma(b=6, a=2)
soma(6, 2)
'''

'''
#empacotamento e desempacotamento
def contador(* num):
    for valor in num:
        print(f"{valor}", end='')
    print(num)


contador(4, 3, 2)
contador(2, 4)
contador(4, 3, 2, 3, 4, 5, 4)
'''

'''
#empacotamento e desempacotamento
def contador(* num):
    tamanho = len(num)
    print(f'recebi os valores {num} e são ao todo {tamanho} números')


contador(4, 3, 2)
contador(2, 4)
contador(4, 3, 2, 3, 4, 5, 4)
'''
'''
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
        
valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
'''
'''
def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(3, 4)
soma(5, 3, 4)
'''