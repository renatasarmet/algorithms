def word_search(matrix, word):
	n_rows = len(matrix)
	if n_rows == 0:
		return False

	n_columns = len(matrix[0])
	word_size = len(word)
	index_word = 0

	for r in range(n_rows):
		for c in range(n_columns):
			if matrix[r][c] == word[index_word]:
				# try left-to-right
				index_word = 1
				aux = c + 1
				while aux < n_columns:
					if matrix[r][aux] == word[index_word]:
						index_word += 1
						aux += 1

						if index_word >= word_size:
							return True
					else:
						break

				# try up-to-down
				index_word = 1
				aux = r + 1
				while aux < n_rows:
					if matrix[aux][c] == word[index_word]:
						index_word += 1
						aux += 1

						if index_word >= word_size:
							return True
					else:
						break

				index_word = 0

	return False


  
matrix = [
  ['F', 'A', 'C', 'I'],
  ['O', 'B', 'Q', 'P'],
  ['A', 'N', 'O', 'B'],
  ['M', 'A', 'S', 'S']]

print(word_search(matrix, 'FOAM'))
# True
