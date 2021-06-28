"""
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento
de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO
nas eleições.
"""


def voto(nasc):
    from datetime import date
    # Escopo de importação: Como só preciso de 'date' dentro da função,
    # eu posso importa-la apenas dentro da função ao invés de importar no escopo global.
    # Isto economiza memória.
    idade = date.today().year - nasc
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    elif 16 <= idade < 18 or idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'


ano = int(input('Em que ano você nasceu? '))
print(voto(ano))
