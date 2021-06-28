teste = []
teste.append('Gustavo')
teste.append(40)
galera = []
galera.append(teste[:]) # Atenção!!! Precisa colocar o [:] pra não gerar um vínculo entre as listas

novagalera = [['João', 19], ['Maria', 25], ['Helena', 18], ['Joaquim', 13]]
print(novagalera[2][1]) # 18

for pessoa in novagalera:
    print(f'{pessoa[0]} tem {pessoa[1]} anos.')

outragalera = []
dado = []
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    outragalera.append(dado[:])
    dado.clear()
print(outragalera)
for p in outragalera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade')
