'''
Crie um programa que vai gerar cinco
números aleatóiros e calcule em uma Tupla.

Depois disso, mostre a listagem de
números gerados e também indique o
menor e o maior valor que estão na
tupla
'''
from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10),)
print(n)
print(f"O maior é: {max(n)}")
print(f"O menor é: {min(n)}")