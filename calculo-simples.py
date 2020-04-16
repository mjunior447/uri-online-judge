"""
Neste problema, deve-se ler o código de uma peça 1,
o número de peças 1, o valor unitário de cada peça 1,
o código de uma peça 2, o número de peças 2
e o valor unitário de cada peça 2.
Após, calcule e mostre o valor a ser pago.
"""

codigo_1 = int(input())
num_pecas_1 = int(input())
valor_unitario_1 = float(input())

codigo_2 = int(input())
num_pecas_2 = int(input())
valor_unitario_2 = float(input())

total_1 = float(num_pecas_1) * valor_unitario_1
total_2 = float(num_pecas_2) * valor_unitario_2

print ("VALOR A PAGAR: R$ %.2f" % (total_1 + total_2))