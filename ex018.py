'''
Exercício Python 018: Faça um programa que leia um ângulo qualquer
e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
https://docs.python.org/3.9/library/math.html
'''
from math import radians, sin, cos, tan

angle = float(input('informe o ângulo: '))
sin = sin(radians(angle))
cos = cos(radians(angle))
tan = tan(radians(angle))

print('seno = {:.2f}\ncosseno = {:.2f}\ntangente = {:.2f}'.format(sin, cos, tan))
