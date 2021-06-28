"""
Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado.
Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(),
mas com uma validação de dados para aceitar apenas valores que seja monetários.
"""
from modulos.ex112.utilidadespackage import moeda, dado

valor = dado.leiadinheiro('Informe um valor: R$')
taxa_aumento = float(input('Informe uma taxa % de aumento: '))
taxa_reducao = float(input('Informe uma taxa % de redução: '))
moeda.resumo(valor, taxa_aumento, taxa_reducao)
