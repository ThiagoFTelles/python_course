"""
Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: Apenas cédulas de 50, 20, 10 e 1
"""

print('=' * 30)
print(f'{"BANCO 2T":^30}')
print('=' * 30)
valor = int(input('Qual valor você quer sacar? '))
total = valor
cedula_atual = 50
qtd_cedulas = 0
while True:
    if total >= cedula_atual:
        total -= cedula_atual
        qtd_cedulas += 1
    else:
        if qtd_cedulas > 0:
            print(f'Você recebe {qtd_cedulas} cédulas de {cedula_atual}')
        qtd_cedulas = 0
        if total == 0:
            break
        elif cedula_atual == 50:
            cedula_atual = 20
        elif cedula_atual == 20:
            cedula_atual = 10
        elif cedula_atual == 10:
            cedula_atual = 1
print('=' * 30)
print(f'{"VOLTE SEMPRE":^30}')
print('=' * 30)
