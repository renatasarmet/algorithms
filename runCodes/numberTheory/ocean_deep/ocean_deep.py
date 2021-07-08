CHECK_NUMBER = 131071

def is_divisible(complete_binary):
 	x = 0
 	for b in complete_binary:
 		x = (x*2 + int(b)) % CHECK_NUMBER
 	return x == 0

binary = input()
while(binary):
	# Reading the complete binary number
	complete_binary = binary
	while(binary[-1] != '#'):
		binary = input()
		complete_binary += binary
	complete_binary = complete_binary[:-1]

	# Checking if it is divisible by CHECK_NUMBER
	if(is_divisible(complete_binary)):
		print("YES")
	else:
		print("NO")

	# ToDo: EOF could be better handled
	try:
		binary = input()
	except:
		binary = None
