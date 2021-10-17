# Given two calendar and two daily_bounds, 
# return free slots of time when both can have meetings 
# with a given duration

# ps: you can assume that both lists are sorted

from collections import deque

def compare_times(t1, t2):
	hour1, minute1 = map(int, t1.split(':'))
	hour2, minute2 = map(int, t2.split(':'))

	time1 = hour1*60 + minute1
	time2 = hour2*60 + minute2

	return time1 - time2 # if it's negative, t1 is bigger, if it's positive, t2 is bigger, if it's 0, both are the same


def get_first_and_last_time(s1, s2, c1, c2, size1, size2):
	first_time = s1[c1][0]

	diff_time2 = compare_times(s1[c1][1], s2[c2][0])

	if diff_time2 < 0: 	# s1 ends before s2 started, so we add just s1
		last_time = s1[c1][1]

	else:	# s2 starts before s1 ends, so we merge both schedules

		diff_time3 = compare_times(s1[c1][1], s2[c2][1])

		if diff_time3 <= 0: # s1 ends before s2, so we add s2 as final
			last_time = s2[c2][1]
		else: # s2 ends before s1, so we add s1 as final
			last_time = s1[c1][1]
		c2 += 1

	c1 += 1

	return c1, c2, first_time, last_time


def join_schedules(schedule1, schedule2):
	## join schedule1 and schedule2
	size1 = len(schedule1)
	size2 = len(schedule2)

	union_schedules = deque()

	c1 = 0
	c2 = 0

	while (c1 < size1) and (c2 < size2): 

		diff_time = compare_times(schedule1[c1][0], schedule2[c2][0])
		if diff_time <= 0: # s1 starts before s2
			c1, c2, first_time, last_time = get_first_and_last_time(schedule1, schedule2, c1, c2, size1, size2)
		else:
			c2, c1, first_time, last_time = get_first_and_last_time(schedule2, schedule1, c2, c1, size2, size1)

		union_schedules.append([first_time, last_time])

	if c1 >= size1: # if c1 is over, just append whats is left in c2 to union_schedules
		for i in range(c2, size2):
			union_schedules.append(schedule2[i])

	if c2 >= size2: # if c2 is over, just append whats is left in c1 to union_schedules
		for i in range(c1, size1):
			union_schedules.append(schedule1[i])

	return union_schedules


def clean_daily_bounds(union_schedules, daily_bound1, daily_bound2):
	# Check daily bounds who starts last
	diff_time = compare_times(daily_bound1[0], daily_bound2[0])

	if diff_time <= 0: 	# if db1 starts first, so db2 is the first available time
		start_bound = daily_bound2[0]
	else:	# if db2 starts first, so db1 is the first available time
		start_bound = daily_bound1[0]

	for i in range(len(union_schedules)):
		diff_time = compare_times(start_bound, union_schedules[i][0])

		if diff_time > 0: 	# s starts before start_bound starts, so we should change it

			diff_time2 = compare_times(start_bound, union_schedules[i][1])

			if diff_time2 > 0: 	# s ends before start_bound ends, so we should remove this element
				union_schedules.popleft()
			else:
				union_schedules[i][0] = start_bound
				break
		else:
			break

	# Check daily bounds who ends last
	diff_time = compare_times(daily_bound1[1], daily_bound2[1])

	if diff_time <= 0: 	# if db1 ends first, so db1 is the last available time
		end_bound = daily_bound1[1]
	else:	# if db2 ends first, so db2 is the last available time
		end_bound = daily_bound2[1]

	for i in range(len(union_schedules)-1,-1,-1):
		diff_time = compare_times(end_bound, union_schedules[i][1])

		if diff_time < 0: 	# end_bound ends before s ends, so we should change it

			diff_time2 = compare_times(end_bound, union_schedules[i][0])

			if diff_time2 < 0: 	# end_bound ends before s starts, so we should remove this element
				union_schedules.pop()
			else:
				union_schedules[i][1] = end_bound
				break
		else:
			break


def add_slot(slots, duration, last_end, next_start):
	diff_time = compare_times(next_start, last_end)
	if diff_time >= duration: # we can make a meeting here
		slots.append([last_end, next_start])


def get_available_slots(duration, schedule, daily_bound1, daily_bound2):
	slots = []
	size = len(schedule)

	## Check daily bounds who starts last
	diff_time = compare_times(daily_bound1[0], daily_bound2[0])

	if diff_time <= 0: 	# if db1 starts first, so db2 is the first available time
		last_end = daily_bound2[0]
	else:	# if db2 starts first, so db1 is the first available time
		last_end = daily_bound1[0]

	## Check intervals in schedule
	for i in range(size):
		next_start = schedule[i][0]
		add_slot(slots, duration, last_end, next_start)
		last_end = schedule[i][1]

	## Check daily bounds who ends first
	diff_time = compare_times(daily_bound1[1], daily_bound2[1])

	if diff_time <= 0: 	# if db1 ends first, so db1 is the last available time
		next_start = daily_bound1[1]
	else:	# if db2 ends first, so db2 is the last available time
		next_start = daily_bound2[1]

	add_slot(slots, duration, last_end, next_start)

	return slots


def find_available_time(duration, schedule1, daily_bound1, schedule2, daily_bound2):
	print("duration = ", duration)
	print("daily_bound1 = ",daily_bound1)
	print("daily_bound2 = ",daily_bound2)
	print()

	## Join schedule1 and schedule2
	union_schedules = join_schedules(schedule1, schedule2) 		# O(size1 + size2)
	print("All busy time together:")
	print(union_schedules)
	print()

	## Clean daily bound as meetings
	clean_daily_bounds(union_schedules, daily_bound1, daily_bound2)		# O(size1 + size2)
	print("All busy time together cleaned respecting daily bounds:")
	print(union_schedules)
	print()

	# Get the available slots
	slots = get_available_slots(duration, union_schedules, daily_bound1, daily_bound2)	# O(size1 + size2)
	print("All available slots:")
	print(slots)



if __name__ == "__main__":

	duration = 30

	schedule1 = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
	daily_bound1 = ['9:00', '20:00']

	schedule2 = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
	daily_bound2 = ['10:00', '18:30']

	### union_schedules = [['9:00', '11:30'], ['12:00', '14:30'], ['14:30', '15:00'],  ['16:00', '18:00']]

	output = find_available_time(duration, schedule1, daily_bound1, schedule2, daily_bound2)		# O(size1 + size2)
	# print(output)

	# output = [['11:30', '12:00'], ['15:00', '16:00'], ['18:00', '18:30']]
