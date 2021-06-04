
available_coins = [50, 25, 10, 5, 1]
# MAX = len(available_coins)

# def coinREC(v, current_i):
# 	if (v == 0):
# 		return 1

# 	sum_ways = 0
# 	for i in range(current_i,MAX): # it is important start in current_i to tell that order does not matter
# 		if (v >= available_coins[i]):
# 			sum_ways += coinREC(v-available_coins[i], i)
# 	return sum_ways


def coinPD(V):
	# for all values of v
	for coin in available_coins: 
		for v in range(coin,V+1):
			MEMO[v] += MEMO[v-coin]
	return MEMO[V]


cents = int(input())
while(cents != None):

	# print(coinREC(cents,0))

	MEMO = [0] * (cents+1)
	MEMO[0] = 1
	print(coinPD(cents))

	# ToDo: EOF could be better handled
	try:
		cents = int(input())
	except:
		cents = None
