# from utils import fatorial, dobro
# É mais recomendado importar todos os módulos, para evitar conflito de funções de mesmo nome em módulos diferentes
import utils # importando o módulo
from uteis import numeros # importando o Grupo numeros do Pacote uteis

num = int(input('Digite um valor: '))
fat = utils.fatorial(num) # usando o módulo
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {utils.dobro(num)}') # usando o módulo

fat = numeros.fatorial(num) # usando o Grupo numeros do Pacote uteis
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {numeros.dobro(num)}') # usando o Grupo numeros do Pacote uteis
