# https://www.urionlinejudge.com.br/judge/pt/problems/view/1019

segundos = int(input())
minutos = 0
horas = 0

if segundos >= 60:
	minutos = segundos // 60
	segundos = segundos % 60

	if minutos >= 60:
		horas = minutos // 60
		minutos = minutos % 60

print(str(horas)+":"+str(minutos)+":"+str(segundos))