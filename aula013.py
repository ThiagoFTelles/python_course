inicio = int(input('INÍCIO - Digite um número: '))
fim = int(input('FIM - Digite um número: '))
passo = int(input('PASSO - Digite um número: '))
for contador in range(inicio, fim+1, passo):
    print(contador)
print('FIM')

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('A soma de todos os valores é {}'.format(s))
