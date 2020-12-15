def tabulation_LCS(x,y,lcs=0):
    m = len(x)
    n = len(y)
    matrix = [[0 for _ in range(n+1)]for _ in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                continue
            elif x[i-1] == y[j-1]:
                matrix[i][j] = 1 + matrix[i-1][j-1]
            else:
                matrix[i][j] = max(matrix[i-1][j],matrix[i][j-1])

    return matrix[m][n]

S1 = "aab"
S2 = "azb"
x = "AGGTAB"
y = "GXTXAB"
print(tabulation_LCS(S1,S2))
print(tabulation_LCS(x,y))