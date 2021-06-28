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
