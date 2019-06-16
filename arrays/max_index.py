def get_diff(a):
    i = n-1
    while(i > 0):
        for j in range(i-1):
            if a[i]-a[j] >= 0:
                print(a[i])
                print(a[j])
                return i-j
        i -=1
    return 0
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print(get_diff(a))
    