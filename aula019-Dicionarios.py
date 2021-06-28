""""
DICIONÁRIOS:
 - São inicializados com  = dict() ou com = {}
 - dicionario = { 'key':'value', 'key2':'value2' }
 - Adicionando uma nova chave: dicionario['newkey']='value'
 - Removendo elementos: del dicionario['key'] -> remove a chave e o valor
"""

filme = {
        'titulo': 'Star Wars',
        'ano': 1977,
        'diretor': 'George Lucas'
         }
print(filme.values()) # dict_values(['Star Wars', 1977, 'George Lucas'])
print(filme.keys()) # dict_keys(['titulo', 'ano', 'diretor'])
print(filme.items(), '\n') # dict_items([('titulo', 'Star Wars'), ('ano', 1977), ('diretor', 'George Lucas')])

for key, value in filme.items():
    print(f'O {key} é {value}')
print()

# Dicionário dentro de uma lista:
locadora = [
        {
        'titulo': 'Star Wars',
        'ano': 1977,
        'diretor': 'George Lucas'
         },
        {
        'titulo': 'Avengers',
        'ano': 2012,
        'diretor': 'Joss W.'
         },
        {
        'titulo': 'Matrix',
        'ano': 1999,
        'diretor': 'Machowski'
         },
            ]
print(locadora[0]['titulo'], '\n') # Star Wars

pessoas = {'nome':'Thiago', 'sexo':'M', 'idade':32}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print('-='*32)
for key in pessoas.keys():
    print(f'{key}')
print('-='*32)
for value in pessoas.values():
    print(f'{value}')
print('-='*32)
del pessoas['sexo']
pessoas['nome'] = '2T'
pessoas['peso'] = 70
for key, value in pessoas.items(): # Não precisa do enumerate()
    print(f'{key} = {value}')
print('-='*32)
estado = {}
brasil = []
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())
    # Preciso criar com .copy() para não gerar vínculo com a variável estado.
    # É semelhante ao fatiamento da lista com [:]
for estado in brasil:
    for key, value in estado.items():
        print(f'{key}:{value}')
    print()
