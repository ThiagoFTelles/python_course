''' Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto
e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa. '''
from math import hypot

cateto_oposto = float(input('Comprimento do cateto oposto: '))
cateto_adjacente = float(input('Comprimento do cateto adjacente: '))

hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2)
hipotenusa_2 = hypot(cateto_oposto, cateto_adjacente)

print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa_2))
