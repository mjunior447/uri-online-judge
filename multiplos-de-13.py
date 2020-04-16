X = int(input())
Y = int(input())

i = X
soma = 0
while(i <= Y):
	if (i % 13 != 0):
		soma += i
	i += 1

print("%d" %soma)