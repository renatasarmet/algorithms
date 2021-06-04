def saleREC(v, current_i):
	# print("--- temos v = ", v)
	if (v == 0):
		return 0

	best_strategy = 0
	for i in range(current_i, N): # for every item
		if (v >= weights[i]):
			best_strategy = max(prices[i]+saleREC(v-weights[i], i+1), best_strategy)
	
	# print(f"para v {v} tenho {best_strategy}")
	return best_strategy


# def saleRECPD(v, current_i):
# 	print("--- temos v = ", v)
# 	if (v == 0):
# 		return 0

# 	if MEMO[v] != -1: # we already calculated it
# 		print(f"sim ja calculei para v {v} com MEMO = {MEMO[v]} ")
# 		return MEMO[v]

# 	MEMO[v] = 0
# 	for i in range(current_i, N): # for every item
# 		if (v >= weights[i]):
# 			MEMO[v] = max(prices[i]+saleRECPD(v-weights[i], i+1), MEMO[v])
	
# 	print(f"para v {v} tenho {MEMO[v]}")
# 	return MEMO[v]


# def saleRECPD(v, current_i):
# 	print("--- temos v = ", v)
# 	if (v == 0):
# 		return 0

# 	if MEMO[v] != -1: # we already calculated it
# 		print(f"sim ja calculei para v {v} com MEMO = {MEMO[v]} ")
# 		return MEMO[v]

# 	best_strategy = 0
# 	for i in range(current_i, N): # for every item
# 		if (v >= weights[i]):
# 			best_strategy = max(prices[i]+saleRECPD(v-weights[i], i+1), best_strategy)
	
# 	MEMO[v] = best_strategy
# 	print(f"para v {v} tenho {MEMO[v]}")
# 	return best_strategy



# def coinRECPD(v, current_i):
# 	print(f"temos v = {v}")
# 	if (v == 0):
# 		return 1

# 	if MEMO[v] != -1: # we already calculated it
# 		print(f"sim ja calculei para v {v} com MEMO = {MEMO[v]} ")
# 		return MEMO[v]

# 	MEMO[v] = 0
# 	for i in range(current_i,MAX): 
# 		if (v >= available_coins[i]):

# 			way = coinRECPD(v-available_coins[i], i)
# 			print(f"---- v = {v}. available_coins[i] = {available_coins[i]}. way = {way}")
# 			# print("memo = ", MEMO)
# 			MEMO[v] += way
# 			print("novo memo = ", MEMO)
# 	return MEMO[v]


# def coinPD(V):
# 	# for all values of v
# 	for v in range(1,V+1):
# 		print("VAMOS COM v = ", v, "MEMO = ", MEMO)
# 		MEMO[v] = 0
# 		for i in range(MAX): 
# 			print(f"para i = {i} coint = {available_coins[i]}, MEMO = ", MEMO)
# 			if (v >= available_coins[i]):
# 				print("v >= available_coins ...")
# 				print(f"se olharmos para v-available_coins[i] = {v-available_coins[i]}, com valor do memo = {MEMO[v-available_coins[i]]}")
# 				print(f"e antes o atual estava {MEMO[v]}")
# 				MEMO[v] += MEMO[v-available_coins[i]]
# 				print("novo memo = ", MEMO)
# 	return MEMO[V]


T = int(input())
for t in range(T):
	N = int(input())

	prices = []
	weights = []

	for n in range(N):
		p, w = map(int,input().split())
		prices.append(p)
		weights.append(w)

	max_weight = []
	G = int(input())
	for g in range(G):
		max_weight.append(int(input()))

	total_value = 0
	# for each person
	for g in range(G):

		g_value = saleREC(max_weight[g],0)

		# MEMO = [-1] * (max_weight[g]+1)
		# g_value = saleRECPD(max_weight[g],0)
		# print("----------------------- g_value = ", g_value)

		total_value += g_value


	# MEMO = [-1] * (cents+1)
	# MEMO[0] = 1
	# print(MEMO)
	# print(coinPD(cents))

	print(total_value)

