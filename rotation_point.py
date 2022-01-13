# https://www.interviewcake.com/question/python3/find-rotation-point

def find_rotation_point(words, start, end):
	if end == start:
		return start
	elif start+1 == end:
		if words[start] > words[end]:
			return end
		return start

	base_word = words[start]

	move = (end - start)//2
	middle = start + move

	middle_word = words[middle]

	if middle_word < base_word:
		rotation = find_rotation_point(words, start, middle)
	else:
		rotation = find_rotation_point(words, middle, end)

	return rotation

words = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote',  # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
]

size = len(words)
print(find_rotation_point(words=words, start=0, end=size-1))
