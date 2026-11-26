#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.

import math

num = float(input('Digite um valor: '))
inteiro = math.trunc(num)

print(f'O valor digitado foi {num} e a sua parte inteira é {inteiro}')