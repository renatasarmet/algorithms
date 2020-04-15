# Is Unique: Implement an algorithm to determine if a string has all unique characters. 

def all_unique_hash(string):
	dic = {}

	for i in string:
		if i not in dic:
			dic[i] = 1
		else:
			return False


	return True


# What if you cannot use additional data structures?

def all_unique_simple(string):
	for i in range(len(string)):
		for j in string[i+1:]:
			if string[i] == j:
				return False

	return True



string = input("Digite a string:")
print("Using hash table.. Unique:", all_unique_hash(string))
print("Without data structures.. Unique:", all_unique_simple(string))