# https://www.urionlinejudge.com.br/judge/pt/problems/view/2867

C = int(input())
for i in range(C):
	N, M = map(int,input().split())

	result = N ** M

	print(len(str(result)))