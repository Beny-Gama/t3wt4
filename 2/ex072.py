'''
Crie um programa que tenha uma tupla
totalmente preenchida com uma contagem por
estenso, zero até vinte.

Seu programa deverá ler um número pelo
tecado (entre 0 e 20) e mostrá-la por
extenso.
'''
e = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
n = -1
while n <= 0 or n >= 20:
    n = int(input('Número entre [0 e 20] '))
print('O número foi: {}.'.format(e[n]))
