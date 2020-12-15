"""
value = [5,3,5]
wt = [1,2,3]
W = 5
size = len(wt)
val = [60,100,120]
wt = [10,20,30]
W = 50
size = len(wt)
"""
val = [0,60,50,70,30]
wt = [0,5,3,4,2]
W = 5
size = len(wt)


def knap(n,w):
    table = [[0 for _ in range(w+1)]for _ in range(n)]

    for i in range(n):
        for j in range(w+1):
            if i==0 or j==0:
                table[i][j] = 0
            elif j>=wt[i]:
                a = val[i] + table[i-1][j-wt[i]]
                b = table[i-1][j]
                table[i][j] = max(a,b)
            else:
                table[i][j] = table[i-1][j]

    return table[n-1][w]

print(knap(size,W))