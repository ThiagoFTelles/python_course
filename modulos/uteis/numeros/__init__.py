def fatorial(num):
    """
    -> Calcula o fatorial de um número.
    :param num: O número a ser calculado.
    :return: O valor do fatorial de um número num.
    """
    cont = 1
    resultado = 1
    while cont <= num:
        resultado *= cont
        cont += 1
    return resultado


def dobro(n):
    return n * 2


def triplo(n):
    return n * 3
