"""
Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
"""
individuo = {}
pessoas = []
somaidades = media = 0
while True:
    individuo.clear() # Sempre limpar os valores antes para não dar problema
    individuo['nome'] = str(input('Nome: '))
    while True:
        individuo['sexo'] = str(input('Sexo [M/F]: '))
        if individuo['sexo'] in 'MmFf':
            break
        else:
            print('Erro! Informe apenas M ou F.')
    individuo['idade'] = int(input('Idade: '))
    somaidades += individuo['idade']
    pessoas.append(individuo.copy())
    while True:
        op = str(input('Cadastrar outra pessoa [S/N]? ')).upper()[0]
        if op in 'SN':
            break
        print('Erro! Responda apenas S ou N.')
    if op == 'N':
        break
print('-='*30)
print(f'Ao todo temos {len(pessoas)} pessoas cadastradas')
media = somaidades / len(pessoas)
print(f'A média de idade é de {media:.1f} anos')
print('As mulheres cadastradas foram: ', end='')
for p in pessoas:
    if p['sexo'] in 'fF':
        print(p['nome'], end=' ')
print(f'\nLista das pessoas que estão acima da média: ')
for p in pessoas:
    if p['idade'] > media:
        for k, v in p.items(): # Estou acessando o indivíduo, que é um dicionário.
            print(f'{k} = {v}', end='; ')
        print()
print('<<< ENCERRADO >>>')
