t = int(input())

# For each test case
for i in range(t):

	# Reading inputs
	n = int(input())

	single_men = []

	list_inverse_pref_w = []
	for j in range(n):
		j_w_pref = list(map(int, input().split()))

		j_inverse_w_pref = [0] * n

		for m_j in range(1,len(j_w_pref)):
			man = j_w_pref[m_j]
			j_inverse_w_pref[man-1] = m_j

		list_inverse_pref_w.append(j_inverse_w_pref)

	list_pref_m = []
	for j in range(n):
		j_m_pref = list(map(int, input().split()))

		single_men.append(j_m_pref[0])

		list_pref_m.append(j_m_pref[1:])

	# Initializing marriages (everyone is single)
	w_husband = [0] * n
	m_wife = [0] * n

	# While there are single men
	while len(single_men) > 0:

		# Get the first man
		m = single_men.pop(0)
		m_pref = list_pref_m[m-1]

		# For each woman
		for w in m_pref:

			w_inverse_pref = list_inverse_pref_w[w-1]	
			currently_husband = w_husband[w-1]

			# If w is free
			if currently_husband == 0:
				# They get engaged
				w_husband[w-1] = m
				m_wife[m-1] = w
				break

			# w is engaged. 
			# If w prefers m than her currently husband
			elif w_inverse_pref[m-1] < w_inverse_pref[currently_husband-1]:
				# They get engaged
				w_husband[w-1] = m
				m_wife[m-1] = w

				# currently_husband becomes single again
				m_wife[currently_husband-1] = 0
				single_men.append(currently_husband)
				break

	# Printing final pairs
	for m in range(len(m_wife)):
		print(m+1, m_wife[m])
