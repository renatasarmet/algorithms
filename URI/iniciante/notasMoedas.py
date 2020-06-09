# https://www.urionlinejudge.com.br/judge/pt/problems/view/1021

# URI não está aceitando, pq?

f = float(input())

notes = [100,50,20,10,5,2]
coins = [1,0.5,0.25,0.1,0.05,0.01]

rest = f
print("NOTAS:")
for note in notes:
	qty =  rest // note
	rest = rest % note

	# print("{qty:0.0f} nota(s) de R$ {note:0.2f}")
	print("%0.0f nota(s) de R$ %0.2f" % (qty, note))

print("MOEDAS:")
for coin in coins:
	qty = rest // coin
	rest = rest % coin

	# print("{qty:0.0f} moeda(s) de R$ {coin:0.2f}")
	print("%0.0f moeda(s) de R$ %0.2f" % (qty, coin))
