def aumetar(preço=0, taxa=0, formato=True):
    resp = preço + (preço * taxa/100)
    return resp if formato is False else moeda(resp)


def diminuir(preço=0, taxa=0, formato=True):
    resp = preço - (preço * taxa/100)
    return resp if formato is False else moeda(resp)


def dobro(preço=0, formato=True):
    resp = preço * 2
    return resp if formato is False else moeda(resp)


def metade(preço=0, formato=True):
    resp = preço / 2
    return resp if formato is False else moeda(resp)


def moeda(preço=0, moeda='R$:'):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')


def resumo(preço=0, aumento=0, redução=0):
    print('-' * 30)
    print('RESULTADO DO VALOR'.center(30))
    print('-' * 30)
    print(f'O Valor Preço:   \t{moeda(preço)}')
    print(f'Metade do Preço: \t{metade(preço)}')
    print(f'Dobro do Preço:  \t{metade(preço)}')
    print(f'{aumento}% de Aumento: \t{aumetar(preço, aumento)}')
    print(f'{redução}% de Redução: \t{diminuir(preço, redução)}')
    print('-' * 30)
