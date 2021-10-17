def calculate_distance(x1, x2, y1, y2, x, y):
    # print("estou analisando x1 = ", x1, "x2=", x2, "y1=", y1, "y2=",y2)
    if y >= y1 and y <= y2:
        dist_y = 0
    else:
        dist_y1 = abs(y1 - y)
        dist_y2 = abs(y2 - y)
        dist_y = min(dist_y1, dist_y2)
    if x >= x1 and x <= x2:
        dist_x = 0
    else:
        dist_x1 = abs(x1 - x)
        dist_x2 = abs(x2 - x)
        dist_x = min(dist_x1, dist_x2)
    # print(dist_y + dist_x)
    return dist_y + dist_x

T = int(input())

for t in range(T):
    K = int(input())
    
    L = [()]*K
    max_size = 9223372036854775807

    min_x = max_size
    min_y = max_size
    max_x = -1
    max_y = -1
    
    for k in range(K):
        x1, y1, x2, y2 = map(int, input().split())
        L[k] = (x1, x2, y1, y2)
        min_x = min(min_x, x1)
        min_y = min(min_y, y1)
        max_x = max(max_x, x2)
        max_y = max(max_y, y2)
    
    # print(L)

    # print("min x =", min_x)
    # print("max x =", max_x)
    # print("min y =", min_y)
    # print("max y =", max_y)

    min_dist = max_size
    best_x = L[0][0]
    best_y = L[0][2]
        
    for x in range(min_x, max_x+1):
        for y in range(min_y, max_y+1):
            # print("******para X= ",x,"Y = ",y )
            dist = 0
            for k in L:
                dist += calculate_distance(k[0], k[1], k[2], k[3], x, y)
            
            # print("total dist =", dist)
            if dist < min_dist:
                min_dist = dist
                # print("--------- ACHEI MIN", min_dist)
                best_x = x
                best_y = y
                # print("para x = ", x, "y = ", y)
    
    # print("min_dist = ", min_dist)
    print(f"Case #{t+1}: {best_x} {best_y}") 
