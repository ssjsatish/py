def find_partition(arr, n):
    summ = sum(arr)
    dp = [[True for i in range(n)] for j in range(rows)]
