def prefix_helper(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    ans = ''
    i = 0
    j = 0
    while i <= n1-1 and j <= n2-1:
        if s1[i] != s2[j]:
            break
        ans +=s1[i]
        i +=1
        j +=1
    return ans

a = ['sapple','apple','application']
prefix = a[0]
for i in range(1,len(a)):
    prefix = prefix_helper(prefix,a[i])
print(prefix)
