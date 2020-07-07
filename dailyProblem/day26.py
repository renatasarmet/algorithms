def courses_to_take(course_to_prereqs):
	queue = []
	order_courses = []
	qty_iterations = 0
	size = 0

	for c in course_to_prereqs:
		queue.append(c)
		size += 1

	while len(queue) > 0:
		course = queue.pop(0)

		ready_to_take = True
		for c in course_to_prereqs[course]:
			if course_to_prereqs[c] is not None: # not taken
				if qty_iterations < size and course in course_to_prereqs[c]: # if I already checked 1 time, no need to check again
					return None

				ready_to_take = False

		if ready_to_take:
			course_to_prereqs[course] = None # taken
			order_courses.append(course)
		else:
			queue.append(course)

		qty_iterations += 1

	return order_courses if qty_iterations > 0 else None


courses = {
  'CSC300': ['CSC100', 'CSC200'], 
  'CSC200': ['CSC100'], 
  'CSC100': []
}
# courses = {
#   'CSC300': ['CSC100', 'CSC200'], 
#   'CSC200': ['CSC300'], 
#   'CSC100': []
# } # None

print(courses_to_take(courses))
# ['CSC100', 'CSC200', 'CSC300']
