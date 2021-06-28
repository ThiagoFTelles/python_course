"""
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um n: ')
"""


def leiaInt(msg):
    num = input(msg)
    while True:
        if num.isnumeric():
            return int(num)
        else:
            print('\033[;31mERRO! Digite um número inteiro válido.\033[m')
            num = input(msg)


n = leiaInt('Digite um nº: ')
print(f'Você digitou o número {n}')
