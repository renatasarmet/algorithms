def get_split_possibilities( n ):
	L = [ ]
	limit = (n//2)+1
	for i in range(1,limit):
		new = [ i, n-i]
		L.append(new)
	return L

def get_max_possibility(P, rod):
	array_dp = [-1]*rod

	array_dp[ 0 ] = P[ 0 ]

	for i in range(1, rod):
		possibilities = get_split_possibilities( i+1 ) # [ [ ], [ ] ] 
		max_i = P[ i ] 
		for p in possibilities:
			total = 0
			for j in p:
				total += array_dp[ j-1 ]
			max_i = max(max_i, total)
		array_dp[ i ] = max_i

	return array_dp[rod-1]

rod = 8

P1 = [1, 5, 8, 9, 10, 17, 17, 20]
print(get_max_possibility(P1, rod))

P2 = [3, 5, 8, 9, 10, 17, 17, 20]
print(get_max_possibility(P2, rod))
