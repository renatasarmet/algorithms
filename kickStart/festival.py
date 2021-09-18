T = int(input())

for x in range(1, T+1):
	D, N, K = map(int, input().split())

	list_attractions = [-1]*N
	max_h = 0

	for i in range(N):
		h, s, e = map(int, input().split())
		list_attractions[i] = (h, s, e)

	list_attractions = sorted(list_attractions, key=lambda x: -x[0])

	happiness = [0]*D
	qtd_a_d = [0]*D

	for a in list_attractions:
		days = [a[0] if a[1] <= d and a[2] >= d else 0 for d in range(1,D+1)]
		happiness = [ x + y if qtd < K else y for x,y,qtd in zip(days, happiness, qtd_a_d)]
		qtd_a_d = [ x + 1 if y > 0 else x for x,y in zip(qtd_a_d, days)] 
		
	print(f'Case #{x}: {max(happiness)}')