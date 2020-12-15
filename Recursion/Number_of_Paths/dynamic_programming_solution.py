def numberOfPaths(m,n):
    count = [[0 for x in range(n)] for y in range(m)]
    print(count)

    for i in range(m):
        count[i][0] = 1
    for j in range(n):
        count[0][j] = 1
    print(count)
    for i in range(1,m):
        for j in range(1,n):
            count[i][j] = count[i-1][j] + count[i][j-1]
            print(count)
    return count[m-1][n-1]

m = 3
n = 3
print(numberOfPaths(3,3))