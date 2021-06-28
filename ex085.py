"""
Crie um programa onde o usuário possa digitar SETE valores numéricos e cadastre-os em uma lista única
que mantenha separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente.
"""
num = [[], []]
valor = 0
for c in range(0, 7): # Eu já sei que são sete valores
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
num[0].sort()
num[1].sort()
print('-='*30)
print(f'Os valores pares foram: {num[0]}')
print(f'Os valores ímpares foram: {num[1]}')
