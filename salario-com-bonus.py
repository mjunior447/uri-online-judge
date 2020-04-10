nome = input();
salario = float(input())
total_vendas = float(input())
comissao = 0.15 * total_vendas
total_a_receber = salario + comissao
print("TOTAL = R$ " + str(round(total_a_receber, 2)))