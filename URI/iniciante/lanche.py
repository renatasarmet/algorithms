# https://www.urionlinejudge.com.br/judge/pt/problems/view/1038

total = 0
cod, qtd = map(int, input().split())
if cod == 1:
	total = 4.00 * qtd
elif cod == 2:
	total = 4.50 * qtd
elif cod == 3:
	total = 5.00 * qtd
elif cod == 4:
	total = 2.00 * qtd
elif cod == 5:
	total = 1.50 * qtd
print("Total: R$ " + str("%.2f" % total))