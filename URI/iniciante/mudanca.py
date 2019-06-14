# https://www.urionlinejudge.com.br/judge/pt/problems/view/2685

import sys
for graus in sys.stdin:
	graus = int(graus.strip())
	if (graus >= 0 and graus < 90) or (graus == 360):
		print("Bom Dia!!")
	elif graus < 180:
		print("Boa Tarde!!")
	elif graus < 270:
		print("Boa Noite!!")
	elif graus < 360:
		print("De Madrugada!!")