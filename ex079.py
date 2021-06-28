"""
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
"""
lista = list()
while True:
    valor = int(input('Digite um valor: '))
    if valor not in lista:
        lista.append(valor)
    else:
        print('Você já digitou este valor, tente outro...')
    continuar = input('Gostaria de continuar [S/N]? ').upper()
    if continuar == 'N':
        break
print(f'Você digitou os valores {sorted(lista)}')
