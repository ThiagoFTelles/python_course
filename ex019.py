'''
Exercício Python 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome dos alunos
e escrevendo na tela o nome do escolhido.
'''
from random import choice

a1 = input('Qual o nome do 1º aluno? ')
a2 = input('Qual o nome do 2º aluno? ')
a3 = input('Qual o nome do 3º aluno? ')
a4 = input('Qual o nome do 4º aluno? ')
lista = [a1, a2, a3, a4]
escolhido = choice(lista)

print('O sortudo foi o {}'.format(escolhido))
