

available_coins = [50, 25, 10, 5, 1]
MAX = len(available_coins)


def coinREC(v, current_coin):
	if (v == 0):
		return 1

	sum_ways = 0
	for i in range(MAX):
		if available_coins[i] <= current_coin: #importante to tell that order does not matter
			if (v >= available_coins[i]):
				sum_ways += coinREC(v-available_coins[i],available_coins[i])
	return sum_ways



cents = float(input())
while(cents != None):

	# MEMO = [-1] * cents

	print(coinREC(cents,available_coins[0]))

	# ToDo: EOF could be better handled
	try:
		cents = float(input())
	except:
		cents = None
