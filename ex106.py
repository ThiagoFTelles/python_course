"""
Faça um mini-sistema que utilize o Interactive Help do Python.
O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
Importante: use cores.
"""
from time import sleep
cores = {
    'sem-cor': '\033[m',
    'vermelha': '\033[0;30;41m',
    'verde': '\033[0;30;42m',
    'amarela': '\033[0;30;43m',
    'azul': '\033[0;30;44m',
    'roxa': '\033[0;30;45m',
    'branca': '\033[0;30;47m'
}


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 'amarela')
    print(cores['branca'], end='')
    help(com)
    print(cores['sem-cor'], end='')
    sleep(2)


def titulo(msg, cor='sem-cor'):
    tam = len(msg) + 4
    print(cores[cor], end='')
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)
    print(cores['sem-cor'], end='')
    sleep(1)


comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 'vermelha')
    comando = str(input('Função ou biblioteca (FIM para sair) > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO', 'vermelha')
