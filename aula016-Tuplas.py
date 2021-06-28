"""
Tuplas:
São IMUTÁVEIS
Podem ter dados de Tipos diferentes
São/podem ser iniciadas com parênteses ()
"""

lanche = 'Hamburger', 'Suco', 'Pizza', 'Pudim'
print(lanche) # ('Hamburger', 'Suco', 'Pizza', 'Pudim')
print(lanche[1]) # Suco
print(lanche[-2]) # Pizza
print(len(lanche)) # 4

for comida in lanche:
    print(f'eu vou comer {comida}')

for cont in range (0, len(lanche)):
    print(lanche[cont])

for pos, comida in enumerate(lanche):
    print(f'o {comida} está na posição {pos}')

print (sorted(lanche)) # Retorna uma [Lista] com os elementos em ordem alfabética

a = 2, 5, 4
b = 5, 8, 1, 2
c = a + b # Concatena
print(c) # (2, 5, 4, 5, 8, 1, 2)
print(c.count(5)) # 2 (o 5 aparece duas vezes)
print(c.index(2)) # 0 (retorna o index da primeira ocorrência)

# Apagar a Tupla da memória
del lanche
