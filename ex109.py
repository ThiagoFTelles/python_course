"""
Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
informando se o valor retornado por elas vai ser ou não formatado pela função moeda(),
desenvolvida no desafio 108.
"""
import modulos.ex109.moeda as moeda

valor = float(input('Informe um valor: R$'))
taxa = float(input('Informe uma taxa %: '))

print(f'Aumentando {taxa:.0f}% de {moeda.moeda(valor)} teremos {moeda.aumentar(valor, taxa, True)}')
print(f'Reduzindo {taxa:.0f}% de {moeda.moeda(valor)} teremos {moeda.diminuir(valor, taxa, True)}')
print(f'O dobro de {moeda.moeda(valor)} teremos {moeda.dobro(valor, True)}')
print(f'A metade de {moeda.moeda(valor)} teremos {moeda.metade(valor, True)}')
