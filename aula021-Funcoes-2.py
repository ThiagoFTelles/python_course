# Interactive help:
"""
 - Para usar eu devo acessar o console do python e digitar help()
 - Depois eu digito alguma função e recebo informações sobre ela, ex: print, len, etc
 - Para sair eu digito quit
 - ou.. no meu programa posso utilizar a function help, ex: help(print)
 - uma outra alternativa é usar o print com .__doc__ ex: print(input.__doc__)
"""
help(print)
print(input.__doc__)

# Docstrings:
"""
 - Serve para explicar alguma coisa, ex: na função def contador(i, f, p)
   eu posso explicar o que significa cada parâmetro (início, fim e passo)
   e outras coisas do código que irão aparecer quando alguém der help(contator)
 - As Docstring começam exatamente na linha abaixo de def
 - Elas são escritas entre três aspas duplas, ex:
"""


def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(c, end=' ')
        c += p
    print('FIM!')


help(contador)
# Parâmetros opcionais:
"""
 - Defino um valor padrão para o parâmetro e ele se torna opcional na chamada da função, ex:
"""


def somar(a, b, c=0):
    print(f'A soma é {a+b+c}')


somar(3, 2, 5) # = 10
somar(b=3, a=2) # = 5
# somar(3) = ERRO, pq não defini o valor padrão de b

# Escopo de variáveis:
"""
 - É o local onde a variável vai existir e o local onde a variável não vai existir
"""


def teste():
    x = 8 # x está em um escopo local, não pode ser chamado fora da função
    print(f'Dentro da função teste, n vale {n}') # Chamando o valor de n do escopo global


n = 2
print(f'No programa principal, n vale {n}') # A variável n está no escopo global
teste()


def teste2(b):
    a = 8
    b += 4
    c = 2
    print(f'A dentro do teste2 vale {a}') # -> Se eu não tivesse uma variável "a" no escopo interno, ele iria retornar o valor de "a" do escopo global
    print(f'B dentro do teste2 vale {b}')
    print(f'C dentro do teste2 vale {c}')


def teste3(b):
    global a # -> Vai manipular a variável "a" global em vez de criar uma variável interna
    a = 10 # -> alterou "a" global
    b += 4
    c = 2
    print(f'A dentro do teste3 vale {a}')
    print(f'B dentro do teste3 vale {b}')
    print(f'C dentro do teste3 vale {c}')


a = 5
print(f'A fora vale {a}')
teste2(a)
teste3(a)
print(f'A fora vale {a} depois da global a ser alterada')

# Retorno de Resultados:
"""
 - São os valores retornados das funções, usando return
"""


def soma(a=0, b=0, c=0):
    s = a+b+c
    return s


print(soma(3, 2, 5)) # 10
r1 = soma(3, 2, 5)
r2 = soma(2, 2)
r3 = soma(1, 5)
print(f'Os resultados foram {r1}, {r2} e {r3}')


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


print(f'O fatorial de 5 é {fatorial(5)}')
