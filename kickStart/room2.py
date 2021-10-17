T = int(input())

for t in range(T):
    K = int(input())
    
    X = [()]*(K*2)
    Y = [()]*(K*2)
    
    for k in range(0,K*2,2):
        x1, y1, x2, y2 = map(int, input().split())
        X[k] = x1
        X[k+1] = x2
        Y[k] = y1
        Y[k+1] = y2

    X.sort()
    Y.sort()

    best_x = X[K-1]
    best_y = Y[K-1]
    
    # print("min_dist = ", min_dist)
    print(f"Case #{t+1}: {best_x} {best_y}") 
