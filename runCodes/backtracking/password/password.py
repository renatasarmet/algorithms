# def print_board(board):
# 	for line in board:
# 		print(line)


# def print_lines_board(lines):
# 	for i in range(NUMBER_OF_LINES):
# 		new_line = [0]*NUMBER_OF_LINES
# 		if lines[i] >= 0 and lines[i]<NUMBER_OF_LINES:
# 			new_line[lines[i]] = 1
# 		print(new_line)


# def valid(lin, col):
# 	# Check if the new queen does not conflict with the others already placed
# 	for i in range(lin):
# 		if i != lin and (output_lines_board[i] == col or (abs(output_lines_board[i]-col) == abs(i-lin))):
# 			return False
# 	return True


# def backtracking(l, best_value):
# 	if (l == NUMBER_OF_LINES):
# 		# We found an available solution
# 		# print("NEW AVAILABLE SOLUTION FOUND:")
# 		# print_lines_board(output_lines_board)

# 		# Now we need to calculate the best configuration
# 		value = 0
# 		for i in range(NUMBER_OF_LINES):
# 			value += input_board[i][output_lines_board[i]]

# 		if value > best_value:
# 			best_value = value

# 	else:
# 		# for each line
# 		for col in range(NUMBER_OF_LINES):
# 			if valid(l, col):
# 				output_lines_board[l] = col
# 				best_value = backtracking(l+1, best_value)

# 	return best_value


digits = list(range(10))

n_words = input()
while(n_words):
	n_words = int(n_words)
	print(n_words)
	words = []
	for i in range(n_words):
		words.append(input())

	n_rules = int(input())
	rules = []
	for i in range(n_rules):
		rules.append(input())

	# backtracking()
	print(words)
	print(n_rules)
	print(rules)

	# ToDo: EOF could be better handled
	try:
		n_words = input()
	except:
		n_words = None

