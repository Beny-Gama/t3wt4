time = list()
jogador = dict()
partidas = list()

print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')

jogador['nome'] = str(input("Nome do Jogador: "))
tot = int(input(f'Quantas Partudas jogadas: '))
for c in range(0, tot):
    partidas.append(int(input(f'    Quantos gols na partida {c+1}: ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)

print('-=' * 30)
print(f'jogador {jogador ["nome"]} jogou {len(jogador["gols"])} partidas')
for i, v in enumerate(jogador['gols']):
    print(f'    => na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')