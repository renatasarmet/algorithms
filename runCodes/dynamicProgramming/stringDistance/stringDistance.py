
def printMat(mat):
	print("---------------")
	for i in mat:
		print(i)
	print("---------------")


def alpha(i, j):
	if str1[i] == str2[j]:
		return 0
	return 1


def alinPD(len1, len2):

	for i in range(1, len1+1):
		MEMO[i][0] = i
		MEMO_TRANSFORM_LIST[i][0] = MEMO_TRANSFORM_LIST[i-1][0] + [f'Delete {i}']
		MEMO_INDEX[i][0] = MEMO_INDEX[i-1][0] - 1
    	
	for j in range(1, len2+1):
 	   	MEMO[0][j] = j
 	   	MEMO_TRANSFORM_LIST[0][j] = MEMO_TRANSFORM_LIST[0][j-1] + [f'Insert {j},{str2[j-1]}']
 	   	MEMO_INDEX[0][j] = MEMO_INDEX[0][j-1] + 1

	for i in range(1, len1+1):
		for j in range(1, len2+1):

			replace = alpha(i-1, j-1) + MEMO[i-1][j-1]
			delete = 1 + MEMO[i-1][j]
			add = 1 + MEMO[i][j-1]

			MEMO[i][j] =  min(replace, delete, add)

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
				MEMO_TRANSFORM_LIST[i][j] = MEMO_TRANSFORM_LIST[i][j-1] + [f'Insert {j},{str2[j-1]}']
				MEMO_INDEX[i][j] = MEMO_INDEX[i][j-1] + 1

	return MEMO[len1][len2], MEMO_TRANSFORM_LIST[len1][len2]


str1 = input()
while(str1 != None):

	str2 = input()

	len1 = len(str1)
	len2 = len(str2)

	MEMO = [[0 for x in range(len2+1)] for y in range(len1+1)] 

	MEMO_TRANSFORM_LIST = [[[] for x in range(len2+1)] for y in range(len1+1)] 

	MEMO_INDEX = [[0 for x in range(len2+1)] for y in range(len1+1)] 

	min_value, transform_list = alinPD(len1, len2)

	print(min_value)
	for i in range(len(transform_list)):
		print(f'{i+1} {transform_list[i]}')

	# ToDo: EOF could be better handled
	try:
		str1 = input()
		print()
	except:
		str1 = None
