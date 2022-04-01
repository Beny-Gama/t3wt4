dado = dict()
gols = list()
geral = list()
total = 0
while True:
    dado['nome'] = str(input('Nome do jogoador: '))
    np = int(input('Nunero de Partida: '))
    for c in range(0, np):
        g = ''
        g = (int(input(f'Quantos gols {dado["nome"]} fez na {c + 1}ª partida: ')))
        gols.append(g)
        total += g
    dado['gols'] = gols
    dado['total'] = total
    geral.append(dado.copy())
    resp = '-1'
    while resp not in "SsNn":
        resp = str(input('Quer Continuar: [N/S] ')).strip()[0]
    if resp in "Nn":
        break
print('-=' * 40)
print('cod nome          gols           total')
cont = 0
for i in geral:
    cont += 1
    print(f'{(i.pop())}, {c["nome"]}          {c["gols"]}           {c["total"]}')


while True:
    resp = int(input('mostrar dados de qual jogador (999 para parar): '))
    for c in geral:
        print(f'{cont}, {c["nome"]}          {c["gols"]}           {c["total"]}')
    if resp == 999:
        break

'''print('-=' * 40)
for k, i in dado.items():
    print(f'No campo {k} tem o valor {i}')
print('-=' * 40)
print(f'O Jogador {dado["nome"]} Jogou {np} partidas')
for c in range(0, np):
    print(f'Na partida {c + 1}, {dado["nome"]} fez {gols[c]} gols.')'''

