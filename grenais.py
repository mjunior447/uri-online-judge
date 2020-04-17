i = 0
vitorias_inter = 0
vitorias_gremio = 0
empates = 0

inter = int(input())
gremio = int(input())

if (inter > gremio):
	vitorias_inter += 1
elif (gremio > inter):
	vitorias_gremio += 1
else:
	empates += 1

while (i != 2):
	print ("Novo grenal (1-sim 2-nao)")
	i = int(input())
	if (i == 1):
		inter = int(input())
		gremio = int(input())
		if (inter > gremio):
			vitorias_inter += 1
		elif (gremio > inter):
			vitorias_gremio += 1
		else:
			empates += 1

grenais = vitorias_gremio + vitorias_inter + empates
print ("%d grenais" %grenais)
print ("Inter: %d" %vitorias_inter)
print ("Gremio: %d" %vitorias_gremio)
print ("Empates: %d" %empates)

if (vitorias_inter > vitorias_gremio):
	print ("Inter venceu mais")
elif (vitorias_gremio > vitorias_inter):
	print ("Gremio venceu mais")
else:
	print ("Nao houve vencedor")