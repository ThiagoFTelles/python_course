"""
Refaça o DESAFIO 009 (tabuada), mostrando a tabuada de um número que o usuário escolher,
só que agora utilizando um laço for.
"""

numero = int(input('Escolha um número: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(numero, c, numero*c))
