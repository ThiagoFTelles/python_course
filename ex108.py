"""
Adapte o código do desafio #107, criando uma função adicional chamada moeda()
que consiga mostrar os números como um valor monetário formatado.
"""
import modulos.ex108.moeda as moeda

valor = float(input('Informe um valor: R$'))
taxa = float(input('Informe uma taxa %: '))

print(f'Aumentando {taxa:.0f}% de {moeda.moeda(valor)} teremos {moeda.moeda(moeda.aumentar(valor, taxa))}')
print(f'Reduzindo {taxa:.0f}% de {moeda.moeda(valor)} teremos {moeda.moeda(moeda.diminuir(valor, taxa))}')
print(f'O dobro de {moeda.moeda(valor)} teremos {moeda.moeda(moeda.dobro(valor))}')
print(f'A metade de {moeda.moeda(valor)} teremos {moeda.moeda(moeda.metade(valor))}')
