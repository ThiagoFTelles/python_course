"""
Faça um programa que tenha uma função chamada área(),
que receba as dimensões de um terreno retangular (largura e comprimento)
e mostre a área do terreno.
"""


def area(l, c):
    print(f'A área de um terreno de {l}m x {c}m é de {l*c:.1f}m²')


print('Controle de terrenos')
print('-' * 20)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)
