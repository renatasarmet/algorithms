
B, S = map(int, input().split())
cont = 1
while (B != 0 or S!=0):

	bachelors = []
	for i in range(B):
		bachelors.append(int(input()))

	spinsters = []
	for i in range(S):
		spinsters.append(int(input()))

	qty_bachelor_left = len(bachelors) - len(spinsters)

	if qty_bachelor_left > 0:
		bachelors.sort(reverse=True)
		print(f'Case {cont}: {qty_bachelor_left} {bachelors[-1]}')
	else:
		print(f'Case {cont}: 0')

	B, S = map(int, input().split())
	cont+=1
