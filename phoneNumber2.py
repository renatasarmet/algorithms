def buildHashTable(): 		#  keys: letters, values: corresponding number
	map_letters = {'a': '2', 'b': '2', 'c': '2', 
					'd': '3', 'e': '3', 'f': '3', 
					'g': '4', 'h': '4', 'i': '4', 
					'j': '5', 'k': '5', 'l': '5',
					'm': '6', 'n': '6', 'o': '6', 
					'p': '7', 'q': '7', 'r': '7', 's': '7',
					't': '8', 'u': '8', 'v': '8', 
					'w': '9', 'x': '9', 'y': '9', 'z': '9'}
	return map_letters
			

def convertToDigits(words):
	map_letters = buildHashTable()
	digits = ['']*len(words)
	for i in range(len(words)):
		d = ""
		for w in words[i]:
			d+= map_letters[w]
		digits[i] = d
	return digits
			

def findSubstrings(phoneNumber, words):

	digits = convertToDigits(words)

	print("PHONE NUMBER = ", phoneNumber)

	found_words = [] 

	for i in range(len(digits)):
		if digits[i] in phoneNumber:
			found_words.append(words[i])

	return found_words


# phoneNumber = input('Type the phone number:')
# words = []

# word = input('Type a word:')
# while(word):
# 	words.append(word)
# 	word = input('Type a word:')

phoneNumber = "3668227"
words = ["foo", "bar", "baz", "footbar", "emo", "cap"]

found_words = findSubstrings(phoneNumber, words)
print('FOUND WORDS:', found_words)
# output should be = ['foo', 'emo', 'footbar', 'bar', 'cap']

