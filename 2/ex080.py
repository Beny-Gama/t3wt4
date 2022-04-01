'''
Crie um programa onde usuário possa digitar cinco
valores nimériocos e cadastre-os uma lista, já na
posição correta de iserção (sem usar o sort()). No
Final, mostre na lsita ordenada na tela.
'''
lista = []
for c in range(0, 5):
    v = int(input('Valor: '))
    if c == 0 or v > lista[-1]:
        lista.append(v)
    else:
        pos = 0
        while pos < len(lista):
            if v <= lista[pos]:
                lista.insert(pos, v)
                break
            pos += 1
print(lista)
