"""
Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(),
que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.
"""
import modulos.ex110.moeda as moeda

valor = float(input('Informe um valor: R$'))
taxa_aumento = float(input('Informe uma taxa % de aumento: '))
taxa_reducao = float(input('Informe uma taxa % de redução: '))
moeda.resumo(valor, taxa_aumento, taxa_reducao)
