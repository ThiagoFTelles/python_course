"""
Faça um programa que tenha uma função chamada escreva(),
que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
"""


def escreva(msg):
    q = len(msg) + 4
    print('~'*q)
    print(f'  {msg}')
    print('~'*q)


escreva('Thiago Telles')
escreva('Python')
