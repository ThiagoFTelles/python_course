def moeda(valor=0, simbolo='R$'):
    return f'{simbolo}{valor:.2f}'.replace('.', ',')


def aumentar(valor=0, taxa=0):
    return valor + (valor * taxa/100)


def diminuir(valor=0, taxa=0):
    return valor - (valor * taxa/100)


def dobro(valor=0):
    return valor * 2


def metade(valor=0):
    return valor / 2
