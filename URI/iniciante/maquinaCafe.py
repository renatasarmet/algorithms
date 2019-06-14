# https://www.urionlinejudge.com.br/judge/pt/problems/view/2670

a1 = int(input())
a2 = int(input())
a3 = int(input())

menor = 2 * a2 + 4 * a3 #andar 1
outraOp = 2 * a1 + 2 * a3 #andar 2
if outraOp < menor: 
	menor = outraOp
outraOp = 4 * a1 + 2 * a2 #andar 3
if outraOp < menor:
	menor = outraOp

print(menor)