"""
Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
"""
time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    total = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))
    partidas.clear()
    for c in range(0, total):
        partidas.append(int(input(f'Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total_gols'] = sum(partidas) # soma os valores da lista 'partidas'
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar [S/N]?')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N...')
    if resp == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*60)
for key, jogador in enumerate(time):
    print(f'{key:^4}', end='')
    for dado in jogador.values():
        print(f'{str(dado):<15}', end='')
    print()
print('-'*60)
while True:
    busca = int(input('Mostrar dados de qual jogador (999 para sair)? '))
    if busca == 999:
        break
    if busca >= len(time) or busca < 0:
        print(f'ERRO: Não existe o código {busca}.')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        print(f'O jogador {time[busca]["nome"]} jogou {len(time[busca]["gols"])} partidas.')
        for i, v in enumerate(time[busca]['gols']):
            print(f'No jogo {i + 1} marcou {v} gols')
        print(f'Foi um total de {time[busca]["total_gols"]} gols.')
    print('-'*60)
print('VOLTE SEMPRE')
