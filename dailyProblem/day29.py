def matrix_spiral_print(M):
	limit_up_rows = 0
	limit_down_rows = len(M) - 1

	if limit_down_rows >= 0 and len(M[0]) > 0:

		limit_left_cols = 0
		limit_right_cols = len(M[0]) - 1

		qty_moves = 0

		while limit_left_cols <= limit_right_cols and limit_up_rows <= limit_down_rows:
			operation = qty_moves % 4

			if operation == 0:
				# start at first index
				col = limit_left_cols
				row = limit_up_rows

				# left to right
				while col <= limit_right_cols:
					print(M[row][col], end=' ')
					col += 1

				# mark as done this whole row
				limit_up_rows += 1

			elif operation == 1:
				col = limit_right_cols
				row = limit_up_rows

				# up to down
				while row <= limit_down_rows:
					print(M[row][col], end=' ')
					row += 1

				# mark as done this whole column
				limit_right_cols -= 1

			elif operation == 2:
				col = limit_right_cols
				row = limit_down_rows

				#  right to left
				while col >= limit_left_cols:
					print(M[row][col], end=' ')
					col -= 1

				# mark as done this whole row
				limit_down_rows -= 1

			else:
				col = limit_left_cols
				row = limit_down_rows

				# up to down
				while row >= limit_up_rows:
					print(M[row][col], end=' ')
					row -= 1

				#  mark as done this whole column
				limit_left_cols += 1

			qty_moves += 1

		print()


grid = [[1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]]
# grid = [[1,  2,  3,  4],
#         [6,  7,  8,  9],
#         [11, 12, 13, 14]]

matrix_spiral_print(grid)
# 1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12
