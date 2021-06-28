# Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep

class bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


print(bcolors.GREEN + """Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA""")

itens = ['PEDRA', 'PAPEL', 'TESOURA']
jogador = int(input(bcolors.BOLD + 'Qual é a sua jogada? '))
computador = randint(0, 2)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')

print(bcolors.WARNING + '-=' * 11)
print('Você jogou {}'.format(itens[jogador]))
print('Computador jogou {}'.format(itens[computador]))
print('-=' * 11 + bcolors.END)

if computador == jogador:
    print('Empate!')
elif computador == 0:
    if jogador == 1:
        print('Você ganhou!')
    else:
        print('Você perdeu!')
elif computador == 1:
    if jogador == 2:
        print('Você ganhou!')
    else:
        print('Você perdeu!')
elif computador == 2:
    if jogador == 0:
        print('Você ganhou!')
    else:
        print('Você perdeu!')
