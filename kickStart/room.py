from sys import maxsize

def calculate_distance(x, x1, x2):
    if x >= x1 and x <= x2:
        dist_x = 0
    else:
        dist_x1 = abs(x1 - x)
        dist_x2 = abs(x2 - x)
        dist_x = min(dist_x1, dist_x2)
    return dist_x


T = int(input())

for t in range(T):
    K = int(input())
    
    L = [()]*K

    min_x = maxsize
    min_y = maxsize
    max_x = -1
    max_y = -1
    
    for k in range(K):
        x1, y1, x2, y2 = map(int, input().split())
        L[k] = (x1, x2, y1, y2)
        min_x = min(min_x, x1)
        min_y = min(min_y, y1)
        max_x = max(max_x, x2)
        max_y = max(max_y, y2)

    min_dist = maxsize
    best_x = L[0][0]
    best_y = L[0][2]

    dist_x = [-1]*K

    for x in range(min_x, max_x+1):
        for k in range(K):
            dist_x[k] = calculate_distance(x, L[k][0], L[k][1])

        for y in range(min_y, max_y+1):
            dist = 0
            for k in range(K):
                dist += calculate_distance(y, L[k][2], L[k][3]) + dist_x[k]
            
            if dist < min_dist:
                min_dist = dist
                best_x = x
                best_y = y
    
    print(f"Case #{t+1}: {best_x} {best_y}") 
