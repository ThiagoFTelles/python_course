def resumo(valor=0, taxa_aumento=10, taxa_reducao=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(valor)}') # \t = tabulação
    print(f'Dobro do preço: \t{dobro(valor, True)}')
    print(f'Metade do preço: \t{metade(valor, True)}')
    print(f'{taxa_aumento:.0f}% de aumento: \t{aumentar(valor, taxa_aumento, True)}')
    print(f'{taxa_reducao:.0f}% de redução: \t{diminuir(valor, taxa_reducao, True)}')
    print('-'*30)


def moeda(valor=0, simbolo='R$'):
    return f'{simbolo}{valor:.2f}'.replace('.', ',')


def aumentar(valor=0, taxa=0, formato=False):
    res = valor + (valor * taxa/100)
    return res if not formato else moeda(res)


def diminuir(valor=0, taxa=0, formato=False):
    res = valor - (valor * taxa/100)
    return res if not formato else moeda(res)


def dobro(valor=0, formato=False):
    res = valor * 2
    return res if not formato else moeda(res)


def metade(valor=0, formato=False):
    res = valor / 2
    return res if not formato else moeda(res)
