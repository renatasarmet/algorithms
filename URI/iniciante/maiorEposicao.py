# https://www.urionlinejudge.com.br/judge/pt/problems/view/1080

maior = int(input())
indice = 1
for i in range(2,101):
	valor = int(input())
	if valor > maior:
		maior = valor
		indice = i

print(maior)
print(indice)