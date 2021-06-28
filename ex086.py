"""
Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.
"""
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] # Já criei as linhas zeradas
for linha in range(0, 3): # 3 linhas
    for coluna in range(0, 3): # 3 colunas
        matriz[linha][coluna] = int(input(f'Digite um valor para a posição [{linha}, {coluna}]: '))
print('-='*30)
for l in range(0, 3): # 3 linhas
    for c in range(0, 3): # 3 colunas
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
