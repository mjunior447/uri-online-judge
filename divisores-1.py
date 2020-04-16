# Ler um número inteiro N e calcular todos os seus divisores.

N = int(input())
i = N
while (i > 0):
	if (N % i == 0):
		print(i)
	i -= 1