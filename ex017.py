#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

import math

oposto = float(input('Me dê o tamanho do cateto oposto: '))
adjacente = float(input('Me dê o tamanho do cateto adjacente: '))

hipotenusa = math.hypot(oposto, adjacente)
print(f'O resultado da hipotenusa é {hipotenusa:.2f}')