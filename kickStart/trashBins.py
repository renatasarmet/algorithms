T = int(input())

for x in range(1, T+1):
    N = int(input())
    S = input()
    
    first_index = -1
    last_index = -1
    sum_walk = 0

    last_indexes = [-1]*N
    for i in range(N-1,-1,-1):
        if S[i] == '1':
            last_index = i
        last_indexes[i] = last_index

    for i in range(N):
        if S[i] == '1':
            first_index = i
        else:
            walk_back = N+2 #big number
            walk_front = N+2 #big number

            if first_index != -1:
                walk_back = i - first_index

            if last_indexes[i] != -1:
                walk_front = last_indexes[i] - i
                    
            sum_walk += min(walk_back, walk_front)
            
    print(f"Case #{x}: {sum_walk}")