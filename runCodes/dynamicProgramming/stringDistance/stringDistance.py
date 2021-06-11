

def printMat(mat):
	print("---------------")
	for i in mat:
		print(i)
	print("---------------")


def alpha(i, j):
	if str1[i] == str2[j]:
		return 0
	return 1


# def alinREC(i, j, transform_list):

# 	print("I = ", i, "J = ", j)

# 	if i == 0:
# 		new_list = transform_list.copy()
# 		for k in range(j,0,-1):
# 			new_list.append(f'Insert {k}')
# 			print(new_list)
# 		return j, new_list

# 	if j == 0:
# 		new_list = transform_list.copy()
# 		for k in range(i,0,-1):
# 			new_list.append(f'Delete {k}')
# 			print(new_list)
# 		return i, new_list


# 	replace, new_list2 = alinREC(i-1,j-1, transform_list)
# 	replace += alpha(i-1, j-1)


# 	delete, new_list2 = alinREC(i-1,j, transform_list)
# 	delete += 1

# 	add, new_list2 = alinREC(i,j-1, transform_list)
# 	add += 1

# 	min_value = min(delete, add, replace)

# 	if delete == min_value:
# 		new_list = new_list2.copy()
# 		new_list.append(f'Delete {i}')
# 		print(new_list)
# 	elif add == min_value:
# 		new_list = new_list2.copy()
# 		new_list.append(f'Insert {i}')
# 		print(new_list)

# 	elif replace == min_value:
# 		new_list = new_list2.copy()
# 		if str1[i-1] != str2[j-1]:
# 			new_list.append(f'Replace {i},{str1[i-1]}')
# 		print(new_list)

# 	return min_value, new_list



def alinPD(len1, len2):

	for i in range(1, len1+1):
		MEMO[i][0] = i
		MEMO_TRANSFORM_LIST[i][0] = MEMO_TRANSFORM_LIST[i-1][0] + [f'Delete {i}']
		MEMO_INDEX[i][0] = MEMO_INDEX[i-1][0] - 1
    	
	for j in range(1, len2+1):
 	   	MEMO[0][j] = j
 	   	MEMO_TRANSFORM_LIST[0][j] = MEMO_TRANSFORM_LIST[0][j-1] + [f'Insert {j},{str2[j-1]}']
 	   	MEMO_INDEX[0][j] = MEMO_INDEX[0][j-1] + 1

	# printMat(MEMO)
	# printMat(MEMO_TRANSFORM_LIST)
	# printMat(MEMO_INDEX)

	for i in range(1, len1+1):
		for j in range(1, len2+1):

			# print("I = ", i, "J = ", j)

			replace = alpha(i-1, j-1) + MEMO[i-1][j-1]
			# print("replace = ", replace)
			delete = 1 + MEMO[i-1][j]
			# print("delete = ", delete)
			add = 1 + MEMO[i][j-1]
			# print("insert = ", add)

			MEMO[i][j] =  min(replace, delete, add)

			# print("min = ", MEMO[i][j])


			if replace == MEMO[i][j]:
				MEMO_INDEX[i][j] = MEMO_INDEX[i-1][j-1]
				if str1[i-1] != str2[j-1]:
					MEMO_TRANSFORM_LIST[i][j] = MEMO_TRANSFORM_LIST[i-1][j-1] + [f'Replace {i+MEMO_INDEX[i-1][j-1]},{str2[j-1]}']
				else:
					MEMO_TRANSFORM_LIST[i][j] = MEMO_TRANSFORM_LIST[i-1][j-1]

			elif delete == MEMO[i][j]:
				MEMO_TRANSFORM_LIST[i][j] = MEMO_TRANSFORM_LIST[i-1][j] + [f'Delete {i+MEMO_INDEX[i-1][j]}']
				MEMO_INDEX[i][j] = MEMO_INDEX[i-1][j] - 1

			elif add == MEMO[i][j]:
				MEMO_TRANSFORM_LIST[i][j] = MEMO_TRANSFORM_LIST[i][j-1] + [f'Insert {i+MEMO_INDEX[i][j-1]},{str2[j-1]}']
				MEMO_INDEX[i][j] = MEMO_INDEX[i][j-1] + 1


			# printMat(MEMO)
			# printMat(MEMO_TRANSFORM_LIST)
			# printMat(MEMO_INDEX)

	return MEMO[len1][len2], MEMO_TRANSFORM_LIST[len1][len2]



str1 = input()
while(str1 != None):

	str2 = input()

	len1 = len(str1)
	len2 = len(str2)

	MEMO = [[0 for x in range(len2+1)] for y in range(len1+1)] 

	MEMO_TRANSFORM_LIST = [[[] for x in range(len2+1)] for y in range(len1+1)] 

	MEMO_INDEX = [[0 for x in range(len2+1)] for y in range(len1+1)] 

	# printMat(MEMO)
	# printMat(MEMO_TRANSFORM_LIST)

	# min_value, transform_list = alinREC(len1, len2, [])

	min_value, transform_list = alinPD(len1, len2)

	# printMat(MEMO)
	# print("final min value = ", min_value)
	# print("final list = ", transform_list)

	print(min_value)
	for i in range(len(transform_list)):
		print(f'{i+1} {transform_list[i]}')


	# ToDo: EOF could be better handled
	try:
		str1 = input()
		print()
	except:
		str1 = None
