
n, d, r = map(int, input().split())

while (n != 0 or d!=0 or r!=0):

	morning_routes = list(map(int, input().split()))
	evening_routes = list(map(int, input().split()))

	morning_routes.sort()
	evening_routes.sort(reverse=True)

	extra_hours = 0
	for i in range(n):
		driver_extra_hour = (morning_routes[i] + evening_routes[i]) - d
		if driver_extra_hour > 0:
			extra_hours += driver_extra_hour

	extra_money = extra_hours * r

	print(extra_money)

	n, d, r = map(int, input().split())
