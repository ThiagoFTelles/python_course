"""
Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso,
de zero até dez. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""

numeros = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez'
while True:
    escolha = int(input('Digite um número entre 0 e 10: '))
    if 0 <= escolha <= 10:
        break
    else:
        print('Tente novamente. ', end = '')
print(f'Você escolheu o número {numeros[escolha]}.')
