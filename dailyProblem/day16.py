def solve_expression(current_expression, value):
	if len(current_expression) == 1 and current_expression[0] == '-': # if it's just the negative sign
		return value * -1

	sign = 1 # 1 indicates plus and -1 indicates negative
	for e2 in current_expression:
		if e2 == '+':
			sign = 1
		elif e2 == '-':
			sign = -1
		else:
			value += int(e2) * sign

	return value


def eval(expression):
	stack = []
	expression = expression.replace(" ", "") # removing spaces

	in_expression = False

	value = 0

	current_expression = []
	for e in expression:
		if e == "(":
			if len(current_expression) > 0:
				stack.append(current_expression)

			current_expression = []
		elif e == ")":
			# the expression I need to solve now is in current_expression 
			value = solve_expression(current_expression, value)

			# pop stack
			current_expression = stack.pop() if len(stack) > 0 else []
		else:
			current_expression.append(e)

	# solve what is left from current_expression
	if len(current_expression) > 0:
		value = solve_expression(current_expression, value)

	return value


print(eval('- (3 + ( 2 - 1 ) )'))
# -4
