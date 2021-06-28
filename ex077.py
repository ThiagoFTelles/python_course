"""
Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""

palavras = ('Viajar', 'Elegante', 'Animal', 'Carro', 'Brasileiro', 'Abacate')

for p in palavras:
    print(f'\nVogais da palavra ({p}): ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f'\033[1;33m{letra.lower()}\033[m', end=' ')
