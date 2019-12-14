# https://www.urionlinejudge.com.br/judge/pt/problems/view/1013

def maiorAB(a,b):
	return (a + b + abs(a-b))/2

a, b, c = map(int, input().split())
print(int(maiorAB(maiorAB(a,b),c)), "eh o maior")
