def is_prime(n):
	return [i for i in range(1,n)if n%i==0]==[1]
count = 1
i = 3
while True:
	if is_prime(i):
		count +=1
	if count == 10001:
		break
	i +=2
print(i)