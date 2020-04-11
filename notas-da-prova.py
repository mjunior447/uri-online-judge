N = int(input())

if(N < 100 & N > 85):
	conceito = 'A'

elif (N < 86 & N > 60):
	conceito = 'B'

elif (N < 61 & N > 35):
	conceito = 'C'

elif (N < 36 & N > 0):
	conceito = 'D'

else:
	conceito = 'E'

print (conceito)