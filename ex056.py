"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho
e quantas mulheres têm menos de 20 anos.
"""

pessoas = []
h_mais_velho_idade = 0
h_mais_velho = {}
mulheres_com_menos_de_20a = 0
soma_idades = 0
for c in range(1, 5):
    print('----- {}ª PESSOA -----'.format(c))
    nome = str(input('- Nome: '.format(c)))
    idade = int(input('- Idade: '.format(c)))
    sexo = str(input('- Sexo: '.format(c)))

    pessoas.insert(len(pessoas)+1, {'nome': nome, 'idade': idade, 'sexo': sexo})
    if pessoas[c-1]['sexo'.lower()] == 'm':
        if pessoas[c-1]['idade'] > h_mais_velho_idade:
            h_mais_velho = pessoas[c-1]
            h_mais_velho_idade = pessoas[c-1]['idade']
    else:
        if pessoas[c - 1]['idade'] < 20:
            mulheres_com_menos_de_20a += 1
    soma_idades += pessoas[c-1]['idade']

soma_idade = 0


for c2 in range(0, len(pessoas)):
        soma_idade += pessoas[c2]['idade']

print('A média de idade do grupo é {}'.format(soma_idade/len(pessoas)))
print('O homem mais velho do grupo é o {}, com {} anos'.format(h_mais_velho['nome'], h_mais_velho_idade))
print('Existem {} mulheres com menos de 20 anos'.format(mulheres_com_menos_de_20a))
