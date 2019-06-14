# https://www.urionlinejudge.com.br/judge/pt/problems/view/1168

n = int(input())

for i in range(0,n):
	v = input()
	total = 0
	for digito in v:
		if digito == '0':
			total += 6
		elif digito == '1':
			total += 2
		elif digito == '2':
			total += 5
		elif digito == '3':
			total += 5
		elif digito == '4':
			total += 4
		elif digito == '5':
			total += 5
		elif digito == '6':
			total += 6
		elif digito == '7':
			total += 3
		elif digito == '8':
			total += 7
		else:
			total += 6

	print(str(total) + " leds")