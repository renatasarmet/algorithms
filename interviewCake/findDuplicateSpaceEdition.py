
def get_duplicate(list_integers):
	list_integers.sort()
	last_number = -1
	for number in list_integers:
		if number == last_number:
			return number
		last_number = number



list_integers = [3,1,5,3,2,5,7,2,3,4]

number =  get_duplicate(list_integers)
print(number)