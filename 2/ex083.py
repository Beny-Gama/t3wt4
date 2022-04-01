'''
Crie um programa onde o usuário digite uma expreção
qualquer que use parénteses. Seu aplicativos deverá
analisar se a expressção possada está com os parametros
amertos e fecados na ordem correta.
'''
frase = str(input('Expreção: ')).strip()
iqual = bool(frase.count('(') - frase.count(')') == 0)
#concomitante = bool(frase.index('(') < frase.index(')'))

print(frase.index('('))
print(frase.index(')'))

'''if iqual and concomitante:    
    print('Valido!')
else:
    print('Invalido!')'''
