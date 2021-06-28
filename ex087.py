"""
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
"""
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] # Já criei as linhas zeradas
soma_pares = maior = soma_coluna = 0

for linha in range(0, 3): # 3 linhas
    for coluna in range(0, 3): # 3 colunas
        matriz[linha][coluna] = int(input(f'Digite um valor para a posição [{linha}, {coluna}]: '))
print('-='*30)
for l in range(0, 3): # 3 linhas
    for c in range(0, 3): # 3 colunas
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            soma_pares += matriz[l][c]
    print()
print('-='*30)
print(f'A soma dos valores pares é {soma_pares}')
for l in range(0, 3):
    soma_coluna += matriz[l][2]
print(f'A soma dos valores da 3ª coluna é {soma_coluna}')
for c in range(0, 3):
    if c == 0 or matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha é {maior}')
