from collections import deque

class TrieNode:
	def __init__(self, value='*', words=[]):
		self.value = value
		self.children = set()
		self.words = words # just used in cases of end of word


class Trie:
	def __init__(self):
		self.root = TrieNode()
		self.map_letters = buildHashTable()


	def add(self, word):
		current_node = self.root
		for c in word:
			c_mapped = self.map_letters[c]
			found_node = False
			for node in current_node.children:
				if node.value == c_mapped:
					current_node = node
					found_node = True
					break
			if not found_node:
				new_node = TrieNode(c_mapped)
				current_node.children.add(new_node)
				current_node = new_node
		
		found_end = False
		for node in current_node.children:
			if node.value == '.':
				found_end = True
				node.words.append(word)

		# create
		if not found_end:
			new_node = TrieNode('.', [word])
			current_node.children.add(new_node)


	def search(self, phoneNumber, start_index, found_words):

		current_node = self.root
		next_index = start_index

		bfs_queue = deque([current_node])

		while len(bfs_queue) > 0:
			current_node = bfs_queue.popleft()

			for node in current_node.children:
				# print('next index = ', next_index)

				# print("olhando o node ", node.value)
				if node.value == '.':  			#   found a word
					found_words.extend(node.words)
					# print("achei essas palavras! ", node.words)
					
				if next_index >= len(phoneNumber):
					break

				# print("phoneNumber[", next_index,"] = ", phoneNumber[next_index])		

				if node.value == phoneNumber[next_index]:
					next_index += 1
					bfs_queue.append(node)
					break # there is just one possible value

		return found_words


	def print_trie(self):
		print("-----------------------------")
		print('PRINTING TRIE')
		current_node = self.root

		dfs_stack = deque([current_node])

		while len(dfs_stack) > 0:
			current_node = dfs_stack.pop()
			print("---> ", current_node.value)

			for node in current_node.children:		
				if node.value == '.':  			#   found a word
					print("---------> . ---> ", node.words)
					
				else:
					dfs_stack.append(node)
		print("-----------------------------")


def buildHashTable( ): 		#  keys: letters, values: corresponding number
	map_letters = {'a': '2', 'b': '2', 'c': '2', 'd': '3', 'e': '3', 'f': '3', 
					'g': '4', 'h': '4', 'i': '4', 'j': '5', 'k': '5', 'l': '5',
					 'm': '6', 'n': '6', 'o': '6', 'p': '7', 'q': '7', 'r': '7', 's': '7',
					't': '8', 'u': '8', 'v': '8', 'w': '9', 'x': '9', 'y': '9', 'z': '9'}
	return map_letters
					

def findSubstrings(phoneNumber, words):

	trie = Trie()
	
	for word in words:
		trie.add(word)

	trie.print_trie()

	print("PHONE NUMBER = ", phoneNumber)

	found_words = [] 

	for start_index in range(len(phoneNumber)):
		found_words = trie.search(phoneNumber, start_index, found_words)

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

