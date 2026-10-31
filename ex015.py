#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. calcule o preço a pagar, sabendo que o carro custa R$60 por dia e 0,50 por km rodado.

dias = int(input('quantos dias alugados? '))
km = float(input('quantos km rodados? '))

pago = (dias * 60) + (km * 0.50)

print(f'o total a pagar é de R$ {pago:.2f}. ')