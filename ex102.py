"""
Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional)
indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
"""


def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não  a conta.
    :return: O valor do fatorial de um número num.
    """
    cont = 1
    resultado = 1
    while cont <= num:
        resultado *= cont
        cont += 1
    if show:
        resp = str()
        for c in range(0, num):
            resp += f'{num-c} x ' if c+1 < num else f'{num-c} = {resultado}'
        return resp
    return resultado


print(fatorial(5, show=True))
print(fatorial(5))


def fatorialGuanabara(n, show=False):
    """
    -> Resolução do Curso em Vídeo
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorialGuanabara(5, show=True))
print(fatorialGuanabara(5))
