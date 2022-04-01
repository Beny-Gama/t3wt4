# Ordem de Prioridade para fazer conta:
# 1 = ()
# 2 = ** #Elevado
# 3 = * / // %
# 4 = + -
n1 = int(input('Um Valor: ' ))
n2 = int(input('outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print(' a soma é: {} \n o produto é: {} \n a divisão é {:.3f} \n'.format(s, m, d), end=' ')
print('divisão inteira: {} \n e potencia {}'.format(di, e))