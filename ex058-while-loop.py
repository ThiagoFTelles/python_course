"""
Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer.
"""

from random import randint

computador = randint(0, 10)
print('Olá! Sou o seu computador e pensei num número entre 0 e 10.\n Será que você consegue adivinhar?')
acertou = False
palpites = 0
jogador = -1
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    palpites += 1
    if jogador < computador:
        print('Mais... tente novamente\n')
    elif jogador > computador:
        print('Menos... tente novamente\n')
    else:
        acertou = True
print('Acertou! Você precisou de {} palpites.'.format(palpites))
