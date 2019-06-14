# https://www.urionlinejudge.com.br/judge/pt/problems/view/1253

n = int(input())

for i in range(n):
	s = input()
	qtd = int(input())
	s = list(s)
	for j in range(len(s)):
		s[j] = chr((((ord(s[j]) - qtd) - 65) % 26) + 65)


	s = ''.join(s)
	print(s)