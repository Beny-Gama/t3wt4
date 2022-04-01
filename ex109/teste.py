from ex109 import moeda

p = float(input('Digite o preço: '))
t = int(input('Digite a Taxa: '))
print(f'A metade de {p} é: {moeda.metade(p)}')
print(f'O dobro de {p} é: {moeda.dobro(p)}')
print(f'A taxa de {p} sobre {t}% é: {moeda.aumetar(p, t)}')
print(f'A taxa de {p} menos {t}% é: {moeda.diminuir(p, t)}')
