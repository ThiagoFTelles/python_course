'''
Exercício Python 020: O mesmo professor do desafio 019 quer sortear
a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
'''
from random import shuffle

a1 = input('Qual o nome do 1º aluno? ')
a2 = input('Qual o nome do 2º aluno? ')
a3 = input('Qual o nome do 3º aluno? ')
a4 = input('Qual o nome do 4º aluno? ')
lista = [a1, a2, a3, a4]
shuffle(lista)

print('Ordem de apresentação:\n1 - {}\n2 - {}\n3 - {}\n4 - {}'.format(lista[0], lista[1], lista[2], lista[3]))
