from math import sqrt
import numpy as np

MAX_DISTANCE = 10000

def calculate_euclidean_distance(p1,p2):
	return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


def divide_and_conquer(sort_x_points):
	qty_points = len(sort_x_points)

	if qty_points < 2:
		return -1

	elif qty_points == 2: #Maybe 3 points
		return calculate_euclidean_distance(sort_x_points[0], sort_x_points[1])

	mid = int(qty_points/2)

	dist1 = divide_and_conquer(sort_x_points[:mid])
	dist2 = divide_and_conquer(sort_x_points[mid:])

	# Find the closest points with one point in each side (within delta)
	if dist1 < 0:
		delta = dist2
	elif dist2 < 0:
		delta = dist1
	else:
		delta = min(dist1, dist2)

	# middle = sort_x_points[mid] is the first point at the right side, which is the closest one to the left side
	middle = sort_x_points[mid]
	min_x = middle[0] - delta
	max_x = middle[0] + delta

	# We build a line crossing middle and a range +delta and -delta from it
	l = mid-1
	while l>0 and sort_x_points[l][0] >= min_x:
		l-=1

	r = mid+1
	while r<qty_points and sort_x_points[r][0] <= max_x:
		r+=1
		
	merge_points = sort_x_points[l:r+1] 

	merge_points.sort(key=lambda x: x[1])
	qty_sort_y_points = len(merge_points)

	min_dist = delta
	for i in range(qty_sort_y_points):
		for j in range(i+1, min(i+16, qty_sort_y_points)):
			new_dist = calculate_euclidean_distance(merge_points[i], merge_points[j])
			min_dist = min(min_dist, new_dist)

	return min_dist


n = int(input())
while n != 0:
	points = []
	for i in range(n):
		new_point = tuple(map(float, input().split()))
		points.append(new_point)

	points.sort(key=lambda x: x[0])

	dist = divide_and_conquer(points)

	if dist >= MAX_DISTANCE or dist < 0:
		print('INFINITY')
	else:
		print(f"{np.float32(dist):.4f}")

	n = int(input())
