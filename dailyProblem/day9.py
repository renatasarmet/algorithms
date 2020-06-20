def check(lst):
	qty = 0 # the number of cases in which [i] > [i+1]
	for i in range(len(lst)-1):
		if(lst[i] > lst[i+1]):
			qty+=1
			if(qty > 1):
				return False

	return True




print(check([13, 4, 7]))
# True
print(check([5,1,3,2,5]))
# False