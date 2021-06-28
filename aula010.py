nome = str(input('Qual é seu nome? '))
if nome == 'Thiago':
    print('Que belo nome!')
else:
    print('Seu nome é tão normal!')
print('Bom dia {}! Vamos jogar?'.format(nome))

"""
Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
O programa deverá escrever na tela se o usuário venceu ou perdeu.
text                background
 
30      black       preto   40
31      red         red     41
32      green       verde   42
33      yellow      amarelo 43
34      blue        azul    44
35      Magenta     Magenta 45
36      cyan        ciano   46
37      grey        cinza   47
97      white       branco  107
"""
from random import randint
from time import sleep
computador = randint(0, 5)
cores = {'limpa':'\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30m',
         'verde': '\033[32m'
         }
print('{}{}{}'.format(cores['verde'], '-=-'*20, cores['limpa']))
print('Vou pensar em um número entre 0 e 5, tente adivinhar...')
print('{}{}{}'.format(cores['verde'], '-=-'*20, cores['limpa']))
jogador = int(input('Em qual número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('Acertou, hacker!')
else:
    print('Burro! Eu pensei no {} e não no {}'.format(computador, jogador))
