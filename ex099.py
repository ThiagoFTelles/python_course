"""
Faça um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""
from time import sleep


def maior(* numeros):
    cont = maior = 0
    print('-='*30)
    print('Analisando so valores passados...')
    for valor in numeros:
        print(valor, end=' ')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi o {maior}')


maior(2, 9, 4, 5, 7, 1)
maior(5)
maior(3, 9, 9)
maior()
