# Check Permutation: Given two strings,write a method to decide if one is a permutation of the other.

def is_permutation(str1, str2):
	dic1 = {}
	dic2 = {}

	for i in str1:
		dic1[i] = dic1.get(i,0) + 1

	for i in str2:
		dic2[i] = dic2.get(i,0) + 1

	if len(dic1) != len(dic2):
		return False

	for i in dic1:
		if dic2.get(i,0) != dic1[i]:
			return False

	return True



str1 = input("String 1:")
str2 = input("String 2:")
print(is_permutation(str1,str2))
