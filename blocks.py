
def find_best_block(blocks, reqs):
	N = len(blocks) # number of blocks

	distance = [{r: N+1 for r in reqs} for i in range(N)]

	# Start the first one
	for r in reqs:
		if blocks[0][r] == True:
			distance[0][r] = 0

	# From left to right
	for i in range(1, N):
		for r in reqs:
			if blocks[i][r] == True:
				distance[i][r] = 0
			else:
				distance[i][r] = distance[i-1][r] + 1


	# Take the answers
	best_block_index = N-1
	max_distance = max([v for k, v in distance[N-1].items()])
	best_block_value = max_distance

	# From right to left, updating the max distance
	for i in range(N-2, -1, -1): # I don't need to do the last one
		for r in reqs:
			distance[i][r] = min(distance[i][r], distance[i+1][r] + 1)

		# Get the max distance and update it
		max_distance = max([v for k, v in distance[i].items()])
		if max_distance < best_block_value:
			best_block_value = max_distance
			best_block_index = i

	print("Distance:", best_block_value)

	return best_block_index


blocks = [
		   {
			"gym": False,
			"school": True,
			"store": False
		   },
		   {
			"gym": True,
			"school": False,
			"store": False
		   },
		   {
			"gym": True,
			"school": True,
			"store": False
		   },
		   {
			"gym": False,
			"school": True,
			"store": False
		   },
		   {
			"gym": False,
			"school": True,
			"store": True
		   }
		]

reqs = ["gym", "school", "store"]

best_block = find_best_block(blocks, reqs)
print("Best block = ", best_block)

# Expected answer = index 3, distance 1

