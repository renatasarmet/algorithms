# https://www.urionlinejudge.com.br/judge/pt/problems/view/1065

cont = 0
for i in range(0,5):
	a = int(input())
	if a % 2 == 0:
		cont += 1

print(str(cont) + " valores pares")