"""
 - Todas as funções em python são identificadas por parênteses no final do nome
 - Para iniciar uma função eu uso def, ex: def myFunction():
 - O PyCharm pede que entre a def e o programa principal tenham duas linhas vazias. (Estética)
"""


def linha():
    print('\n', '-='*40, '\n')


def titulo(texto):
    print('-' * 30)
    print(f'{texto.upper():^30}')
    print('-' * 30)


def somaab(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A + B = {s}')


# Programa principal:
titulo('SOMA')
somaab(2, 5)
titulo('SOMA')
somaab(b=2, a=5) # Posso explicitar os valores dos parâmetros

linha()
# EMPACOTAMENTO: Posso definir uma quantidade dinâmica de parâmetros usando asterisco *
# O empacotamento retorna uma Tupla com os valores passados


def contador(* vals):
    tamanho = len(vals)
    print(f'Recebi os valores {vals} e são ao todo {tamanho} números!')


contador(1, 3, 77, 9)
linha()


def soma(* val):
    s = 0
    for num in val:
        s += num
    print(f'Somando so valores {val} temos {s}')


soma(5,2)
soma(5,2,3,7)

# USANDO LISTAS:
linha()


def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


valores = [2, 5, 7, 9]
dobra(valores)
print(valores)
