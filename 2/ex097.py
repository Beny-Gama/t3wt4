'''
Faça um programa que tenha uma função chamada
escreva(), que receba um texto qualquer como
parâmetro e mostre uma mensagem com tamanho
adaptável.
ex:
escreva()
saida:
~~~~~~~~~~~~
Olá, Mundo!
~~~~~~~~~~~~
'''


def escreva(frs):
    print('~' * (len(frs) + 4))
    print(f' {frs} ')
    print('~' * (len(frs) + 4))


escreva(str(input('Frase: ')))
