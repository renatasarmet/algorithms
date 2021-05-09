def backtracking(cont, password, rule):
	if (cont == len(rule)):
		# We found an available solution
		print(password)
	else:
		# for each line
		current_rule = rule[cont]
		set_character = digits if current_rule == '0' else words
		for char in set_character:
			backtracking(cont+1, password+str(char), rule)


digits = list(range(10))

n_words = input()
while(n_words):
	n_words = int(n_words)
	words = []
	for i in range(n_words):
		words.append(input())

	n_rules = int(input())
	rules = []
	for i in range(n_rules):
		rules.append(input())

	print("--")

	for rule in rules:
		backtracking(cont=0, password='', rule=rule)

	# ToDo: EOF could be better handled
	try:
		n_words = input()
	except:
		n_words = None
