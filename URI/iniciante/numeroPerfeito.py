# https://www.urionlinejudge.com.br/judge/pt/problems/view/1164

n = int(input())

for i in range(n):
	x = int(input())
	list = []
	total = 0
	for j in range(1,(x//2)+1):
		if x % j == 0:
			total += j

	if total == x:
		print(str(x) + " eh perfeito")
	else:
		print(str(x) + " nao eh perfeito")