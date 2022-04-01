import moeda

p = float(input('Digite o preço: '))
t = int(input('Digite a Taxa: '))
print(f'A metade de {moeda.moeda(p)} é: {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é: {moeda.moeda(moeda.dobro(p))}')
print(f'A taxa de {moeda.moeda(p)} sobre {t}% é: {moeda.moeda(moeda.aumetar(p, t))}')
print(f'A taxa de {moeda.moeda(p)} menos {t}% é: {moeda.moeda(moeda.diminuir(p, t))}')
