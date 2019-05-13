def reduce_to_one(n):
    if n == 1:
        return 1
	ans = 0
    temp = n
    for i in range(1, n):
        ans = i+temp + i*temp
        ans = ans % 1000000007
        temp = ans
    return ans
for _ in range(int(input())):
    n = int(input())
    print(reduce_to_one(n))