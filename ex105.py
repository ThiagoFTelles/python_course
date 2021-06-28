"""
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione também as docstrings dessa função para consulta pelo desenvolvedor.
"""


def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas (aceita várias)
    :param sit: (opcional), indica se deve ou não mostrar a situação do aluno.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    resp = {
        'total': len(n),
        'maior': max(n),
        'menor': min(n),
        'média': sum(n) / len(n)
    }
    if sit:
        if resp['média'] >= 7:
            resp['situação'] = 'BOA'
        elif resp['média'] >= 5:
            resp['situação'] = 'REGULAR'
        else:
            resp['situação'] = 'RUIM'
    return resp


dados = notas(5, 3, 10, 5, sit=True)
print(dados)
help(notas)
