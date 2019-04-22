def print_board(a):
    for i in range(9):
        for j in range(9):
            print(a[i][j], end = '')


for _ in range(int(input())):
    l = list(map(int, input().split()))
    a =[[0 for i in range(9)] for j in range(9)]
    k = 0
    for i in range(9):
        for j in range(9):
            a[i][j] = l[k]
            k +=1
    ans = solve
    
