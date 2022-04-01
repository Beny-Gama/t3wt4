'''
Crie um programa onde o usuário digite uma expreção
qualquer que use parénteses. Seu aplicativos deverá
analisar se a expressção possada está com os parametros
amertos e fecados na ordem correta.
'''
pilha = []
ex = str(input('Expreção: '))
for simb in ex:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua Expreção deu CERTO!')
else:
    print('Sua Expreção deu ERRADO!')
