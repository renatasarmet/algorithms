def print_array(array):
	for line in array:
		print(line)

# Note: here x and y of a matrix are different then what we are used to (like in C)
# instead of matrix[x][y] we use matrix[y][x] to have the same effect

def go_up(array, size, x, y, color, new_color):
	go_left(array, size, x, y, color, new_color)
	go_right(array, size, x+1, y, color, new_color)


def go_down(array, size, x, y, color, new_color):
	go_left(array, size, x, y, color, new_color)
	go_right(array, size, x+1, y, color, new_color)


def go_left(array, size, x, y, color, new_color):
	while((x >= 0) and (array[y][x] == color)):
		array[y][x] = new_color
		if((y > 0) and (array[y-1][x] == color)):
			go_up(array, size, x, y-1, color, new_color)
		if((y < size-1) and (array[y+1][x] == color)):
			go_down(array, size, x, y+1, color, new_color)
		x -=1


def go_right(array, size, x, y, color, new_color):
	while((x < size) and (array[y][x] == color)):
		array[y][x] = new_color
		if((y > 0) and (array[y-1][x] == color)):
			go_up(array, size, x, y-1, color, new_color)
		if((y < size-1) and (array[y+1][x] == color)):
			go_down(array, size, x, y+1, color, new_color)
		x +=1


def fill(array, size, x_point, y_point, new_color):
	print("----FILL----")
	color = array[y_point][x_point]
	if(color == new_color):
		print("Great! We don't need to do anything")
	else:
		go_left(array, size, x_point, y_point, color, new_color)
		go_right(array, size, x_point+1, y_point, color, new_color)


# ---- main ----

print("Matrix:")

array = [	[1,3,1,1,1,1,1],
			[1,0,1,0,2,1,1],
			[1,0,0,0,1,0,1],
			[1,0,0,0,0,0,1],
			[1,0,1,0,1,0,0],
			[1,1,0,1,1,1,0],
			[1,0,1,1,1,0,0]]


size = len(array)
x_point = 2
y_point = 2
new_color = 8


print_array(array)

print("point: {},{}".format(x_point,y_point))
print("new color:", new_color)

fill(array, size, x_point, y_point, new_color)

print_array(array)
