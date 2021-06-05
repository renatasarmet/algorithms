def salePD(max_w):
	for i in range(N):
	    for j in range(max_w, weights[i]-1, -1):
	        # getting max value between x[j] and x[j-W[i]] plus price[i]
	        MEMO[j] = max(MEMO[j], MEMO[j - weights[i]] + prices[i])
	return MEMO[max_w]


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
		MEMO = [0] * (max_weight[g]+1)
		total_value += salePD(max_weight[g])

	print(total_value)
