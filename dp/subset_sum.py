def isSubsetSum(arr,n,sum):
    dp=([[False for i in range(sum+1)] for i in range(n+1)])
    #print(dp)
    for i in range(n+1): 
        dp[i][0] = True
        print(dp)
        for i in range(1,sum+1): 
            dp[0][i]=False
        for i in range(1,n+1): 
            for j in range(1,sum+1): 
                if j<arr[i-1]:
                    dp[i][j] = dp[i-1][j]
                if j>=arr[i-1]:
                    dp[i][j] = (dp[i-1][j] or dp[i - 1][j-arr[i-1]])
    return dp[n][sum] 
if __name__=='__main__': 
	arr = [5,2,3,1,0,7] 
	sum = 9
	n =len(arr) 
	if (isSubsetSum(arr, n, sum) == True): 
		print("Found a dp with given sum") 
	else: 
		print("No dp with given sum") 