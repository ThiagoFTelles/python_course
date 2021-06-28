# Operadores aritméticos:
# + Adição
# - Subtração
# * Multiplicação
# / Divisão
# // Divisão Inteira
# ** Potência
# % Resto da Divisão

# Ordem de Precedência:
# 1: ()
# 2: **
# 3: * / // %
# 4: + -

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ^ n2
# Casas decimais: Se eu quiser colocar duas casas decimais eu uso {:.2f} -> o f significa flutuantes
print('A soma é {}, o produto é {}, a divisão é {:.2f}\nA divisão inteira é {} a potência é {}'.format(s, m, d, di, e))

# Quebra de linha:
#  Posso adicionar \n para quebrar a linha,
#  Ou posso juntar dois prints sem quebrar a linha, colocando print('Alguma coisa {}'.format(x), end='')
print('Esta linha', end=' ')
print('vai ficar junto com esta')

# formatando a saída de dados
nome = input('Qual é o seu nome? ')

# Caracteres: {:20} faz a resposta ocupar 20 caracteres, mesmo se ela for menor
# Alinhamento: à direita {:>20} ou à esquerda {:<20}, ou centralizar {:^20}
print('Prazer em te conhecer {:^20}'.format(nome))

# Símbolos: No código abaixo ele vai preencher os espaços vazios com sinal de =
# OBS: Nesta versão do python (3.9) precisa colocar um f antes das aspas
print(f'Prazer em te conhecer {nome.upper():=^20}')
