# https://www.urionlinejudge.com.br/judge/pt/problems/view/1091

k = int(input())
while k != 0:
	n, m = map(int, input().split())
	for i in range(0, k):
		x, y = map(int, input().split())
		if n == x or m == y:
			print("divisa")
		elif x < n:
			if y < m:
				print("SO")
			else:
				print("NO")
		else:
			if y < m:
				print("SE")
			else:
				print("NE")

	k = int(input())