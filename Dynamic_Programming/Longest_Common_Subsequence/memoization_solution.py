def dojo_memoization(x,y,m,n,table):
    if table[m][n]!=-1:
        return table[m][n]
    if n==0 or m==0:
        result = 0
    elif x[m-1]==y[n-1]:
        result = 1 + dojo_memoization(x,y,m-1,n-1,table)
    else:
        tmp1 = dojo_memoization(x,y,m-1,n,table)
        tmp2 = dojo_memoization(x,y,m,n-1,table)
        result =  max(tmp1,tmp2)
    table[m][n] = result
    return result

S1 = "aab"
S2 = "azb"
x = "AGGTAB"
y = "GXTXAB"

table = [[-1 for iter in range(len(S2)+1)]for iter1 in range(len(S1)+1)]
print(dojo_memoization(S1,S2,len(S1),len(S2),table))
print(table)
print(dojo_memoization(x,y,len(x),len(y),table=[[-1 for _ in range(len(y)+1)] for _ in range(len(x)+1)]))

