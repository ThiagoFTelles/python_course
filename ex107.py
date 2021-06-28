"""
Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(),
diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções.
"""
import modulos.ex107.moeda as moeda

valor = float(input('Informe um valor: R$'))
taxa = float(input('Informe uma taxa %: '))
print(f'Aumentando {taxa}% de {valor} teremos R${moeda.aumentar(valor, taxa)}')
print(f'Reduzindo {taxa}% de {valor} teremos R${moeda.diminuir(valor, taxa)}')
print(f'O dobro de {valor} teremos R${moeda.dobro(valor)}')
print(f'A metade de {valor} teremos R${moeda.metade(valor)}')
