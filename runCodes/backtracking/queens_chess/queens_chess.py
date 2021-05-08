def print_board(board):
	for line in board:
		print(line)


def print_lines_board(lines):
	for i in range(NUMBER_OF_LINES):
		new_line = [0]*NUMBER_OF_LINES
		if lines[i] >= 0 and lines[i]<NUMBER_OF_LINES:
			new_line[lines[i]] = 1
		print(new_line)


def valid(lin, col):
	# Check if the new queen does not conflict with the others already placed
	for i in range(lin):
		if i != lin and (output_lines_board[i] == col or (abs(output_lines_board[i]-col) == abs(i-lin))):
			return False
	return True


def backtracking(l, best_value):
	if (l == NUMBER_OF_LINES):
		# We found an available solution
		# print("NEW AVAILABLE SOLUTION FOUND:")
		# print_lines_board(output_lines_board)

		# Now we need to calculate the best configuration
		value = 0
		for i in range(NUMBER_OF_LINES):
			value += input_board[i][output_lines_board[i]]

		if value > best_value:
			best_value = value

	else:
		# for each line
		for col in range(NUMBER_OF_LINES):
			if valid(l, col):
				output_lines_board[l] = col
				best_value = backtracking(l+1, best_value)

	return best_value


NUMBER_OF_LINES = 8

k = int(input())

for ki in range(k):
	# Each line should be in one column
	# So we have an array that each index represents one line
	# And the value corresponds to which column it is
	# We start with -1 so we didn't put it yet
	output_lines_board = [-1]*NUMBER_OF_LINES

	# Read the input board
	input_board = []
	for i in range(NUMBER_OF_LINES):
		line = list(map(int, input().split()))
		input_board.append(line)

	# print("INPUT BOARD:")
	# print_board(input_board)

	# print("INITIAL OUTPUT BOARD:")
	# print_lines_board(output_lines_board)
	# print("----->", output_lines_board)

	best_value = backtracking(l=0, best_value=0)

	print('{:>5}'.format(best_value))
