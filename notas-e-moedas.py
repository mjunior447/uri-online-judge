valor = int(input())

if (valor >= 100):
	notas_100 = int(valor / 100)
	valor -= notas_100 * 100
	print ("notas de 100: " + str(notas_100))

if (valor >= 50):
	notas_50 = int(valor / 50)
	valor -= notas_50 * 50
	print ("notas de 50: " + str(notas_50))

if (valor >= 20):
	notas_20 = int(valor / 20)
	valor -= notas_20 * 20
	print ("notas de 20: " + str(notas_20))

if (valor >= 10):
	notas_10 = int(valor / 10)
	valor -= notas_10 * 10
	print ("notas de 10: " + str(notas_10))

if (valor >= 5):
	notas_5 = int(valor / 5)
	valor -= notas_5 * 5
	print ("notas de 5: " + str(notas_5))

if (valor >= 2):
	notas_2 = int(valor / 2)
	valor -= notas_2 * 2
	print ("notas de 2: " + str(notas_2))

if (valor != 0):
	moedas_1 = valor
	print ("moedas de 1 real: " + str(moedas_1))

