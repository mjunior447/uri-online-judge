""" 
Leia um valor inteiro X. 
Em seguida apresente os 6 valores ímpares consecutivos a partir de X, 
um valor por linha, inclusive o X ser for o caso.
"""

X = int(input())

qtd_valores = 0
valores = []

while (qtd_valores < 6):
	if (X % 2 != 0):
		valores.append(X)
		qtd_valores += 1

	X += 1

for i in range(0, 5):
	print (valores[i])