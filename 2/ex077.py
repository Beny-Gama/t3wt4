'''
Crie um programa que tenha uma tupla
com várias palavras (Não usar acentos).
depois disso, você deve mostrar, para
cada palavra, quais sção as suas vogais.
'''

palavras = ('Tratado', 'torpido', 'pulsante', 'Catartico', 'Marmoreio', 'Reluzende',
            'Mastodontico', 'Cornoalha', 'Coerente', 'Conteudista', 'Ambivalente',
            'Insurgente', 'Imponente')

for p in palavras:
    print(f'\nPara cada {p} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end='')
