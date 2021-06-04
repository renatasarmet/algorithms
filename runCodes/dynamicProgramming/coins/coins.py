
available_coins = [50, 25, 10, 5, 1]
MAX = len(available_coins)
MAX_CENTS = 7489 
MEMO = [-1] * (MAX_CENTS+1)

def coinREC(v, current_i):
	print(f"temos v = {v}")
	if (v == 0):
		return 1

	sum_ways = 0
	for i in range(current_i,MAX): # it is important start in current_i to tell that order does not matter
		if (v >= available_coins[i]):
			sum_ways += coinREC(v-available_coins[i], i)
	return sum_ways

# PROBLEMA EM PD... ELE ACHA QUE A ORDEM IMPORTA

def coinRECPD(v, current_i):
	print(f"temos v = {v}")
	if (v == 0):
		return 1

	if MEMO[v] != -1: # we already calculated it
		print(f"sim ja calculei para v {v} com MEMO = {MEMO[v]} ")
		return MEMO[v]

	MEMO[v] = 0
	for i in range(current_i,MAX): # it is important start in current_i to tell that order does not matter
		if (v >= available_coins[i]):

			way = coinRECPD(v-available_coins[i], i)
			print(f"---- v = {v}. available_coins[i] = {available_coins[i]}. way = {way}")
			# print("memo = ", MEMO)
			MEMO[v] += way
			print("novo memo = ", MEMO)
	return MEMO[v]


def coinPD(V):
	# for all values of v
	for v in range(1,V+1):
		print("VAMOS COM v = ", v, "MEMO = ", MEMO)
		MEMO[v] = 0
		for i in range(MAX): # it is important start in j to tell that order does not matter
			print(f"para i = {i} coint = {available_coins[i]}, MEMO = ", MEMO)
			if (v >= available_coins[i]):
				print("v >= available_coins ...")
				print(f"se olharmos para v-available_coins[i] = {v-available_coins[i]}, com valor do memo = {MEMO[v-available_coins[i]]}")
				print(f"e antes o atual estava {MEMO[v]}")
				MEMO[v] += MEMO[v-available_coins[i]]
				print("novo memo = ", MEMO)
	return MEMO[V]


cents = int(input())
while(cents != None):

	# print(coinREC(cents,0))

	# MEMO = [-1] * (cents+1)
	# MEMO[0] = 1
	# print(MEMO)
	# print(coinRECPD(cents,0))

	MEMO = [-1] * (cents+1)
	MEMO[0] = 1
	print(MEMO)
	print(coinPD(cents))

	# ToDo: EOF could be better handled
	try:
		cents = int(input())
	except:
		cents = None
