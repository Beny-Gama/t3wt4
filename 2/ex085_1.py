lista = []
dado = []

for c in range(0, 7):
    dado.append(int(input('Numero: ')))
for c in dado:
    if c % 2 == 0:
        lista.append(dado)
lista.append(dado[:])
for c in dado:
    if c % 2 == 1:
        lista.append(dado[1])

print(f'{lista[0]} são pares.')
print(f'{lista[1]} sáo impares.')
