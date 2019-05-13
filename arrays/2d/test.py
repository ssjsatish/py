a = [[i for i in range(2)] for j in range(2)]
print(a)
for i in range(2):
    for j in range(2):
        print(a[i][j], end=" ")
    print()