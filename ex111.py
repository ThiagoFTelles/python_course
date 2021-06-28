"""
Crie um pacote chamado utilidadespackage que tenha dois módulos internos chamados moeda e dado.
Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote
e mantenha tudo funcionando.
"""
from modulos.ex111.utilidadespackage import moeda

valor = float(input('Informe um valor: R$'))
taxa_aumento = float(input('Informe uma taxa % de aumento: '))
taxa_reducao = float(input('Informe uma taxa % de redução: '))
moeda.resumo(valor, taxa_aumento, taxa_reducao)
