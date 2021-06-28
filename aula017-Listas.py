# [LISTAS]

lanche = ['hotdog', 'hamburger', 'suco', 'pizza', 'sorvete', 'cookie']

# Para adicionar um elemento no final da Lista eu uso lanche.append('novo elemento')
# Para adicionar um elemento em uma posição específica eu uso lanche.insert(0, 'novo elemento')

"""
Para apagar um elemento na posição 3 posso fazer:
del lanche[3]
ou
lanche.pop(3) -> OBS, o .pop() normalmente é usado para remover o último elemento
ou
lanche.remove('pizza') -> remove apenas a primeira ocorrência encontrada
"""

# Para verificar antes de remover eu uso o if 'pizza' in lanche: lanche.remove('pizza')
lista_vazia = [] # ou list()
for cont in range(0, 5):
    lista_vazia.append(int(input('Digite um número: ')))

valores = list(range(4, 11)) # [4, 5, 6, 7, 8, 9, 10]

unordered = [8, 2, 4, 9, 6, 7, 3]
unordered.sort() # ordenou a lista
print(unordered) # [2, 3, 4, 6, 7, 8, 9]
unordered.sort(reverse=True) # inverteu a lista
print(unordered) # [9, 8, 7, 6, 4, 3, 2]

a = [2, 4, 6, 8]
b = a # criei uma conexão entre as listas, e não apenas uma cópia
b[2] = 7 # Ele altera a lista "a" e também a lista "b" porque eu igualei (criei um vínculo entre) elas
c = a[:] # agora eu criei apena suma cópia, sem conexão entre elas
b[2] = 0 # altera apenas em "c", "a" permanece inalterada
