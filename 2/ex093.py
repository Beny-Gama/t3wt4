dado = dict()
gols = list()
total = 0
dado['nome'] = str(input('Nome do jogoador: '))
np = int(input('Nunero de Partida: '))
for c in range(0, np):
    g = 0
    g = (int(input(f'Quantos gols {dado["nome"]} fez na {c + 1}ª partida: ')))
    gols.append(g)
    total += g
dado['gols'] = gols
dado['total'] = total
print('-=' * 40)
print(dado)
print('-=' * 40)
for k, i in dado.items():
    print(f'No campo {k} tem o valor {i}')
print('-=' * 40)
print(f'O Jogador {dado["nome"]} Jogou {np} partidas')
for c in range(0, np):
    print(f'Na partida {c + 1}, {dado["nome"]} fez {gols[c]} gols.')

