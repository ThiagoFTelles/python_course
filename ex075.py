"""
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
"""
numeros = tuple(int(input('Digite um número: ')) for c in range(1, 5))

print(f'O numero nove aparece {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'Valor 3 foi digitado pela primeira vez na {numeros.index(3) + 1}ª posição')
else:
    print('Não foi digitado valor 3')
print('Os valores pares digitados foram: ', end=' ')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
