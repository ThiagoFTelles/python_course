"""
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python.
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
"""
from random import randint
from time import sleep
from operator import itemgetter
resultados = {
    'Jogador 1': randint(1, 6),
    'Jogador 2': randint(1, 6),
    'Jogador 3': randint(1, 6),
    'Jogador 4': randint(1, 6)
    }
ranking = []
print('Valores sorteados:')
for k, v in resultados.items():
    print(f'Jogador {k} tirou {v}')
    sleep(1)
ranking = sorted(resultados.items(), reverse=True, key=itemgetter(1)) # Ele vai organizar por valores (índice 1)
print('Os melhores foram:')
print(ranking) # [('Jogador 2', 4), ('Jogador 1', 3), ('Jogador 3', 3), ('Jogador 4', 1)]
for i, v in enumerate(ranking):
    print(f'{i+1}º Lugar: {v[0]} com {v[1]} pontos!')
