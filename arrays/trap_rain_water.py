def total_water(a, n):
    left = [0]*n
    right = [0]*n
    water = 0
    left[0] = a[0]
    right[n-1] = a[n-1]
    for i in range(1,n):
        left[i] = max(left[i],left[i-1])
    for i in range(n-2,-1,-1):
        right[i] = max(right[i+1], right[i])
    for i in range(0,n):
        water += min(left[i], right[i]) - a[i]
    print(water)
    #return water
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    total_water(a,n)