def dojo_recursive(x,y,m,n):
    if n==0 or m==0:
        return 0
    if x[m-1] == y[n-1]:
        return (1 + dojo_recursive(x,y,n-1,m-1))
    else:
        tmp1 = dojo_recursive(x,y,n-1,m)
        tmp2 = dojo_recursive(x,y,n,m-1)
        return max(tmp1,tmp2)



S1 = "aab"
S2 = "azb"
x = "AGGTAB"
y = "GXTXAB"
# print(LCS(S1,S2))
# print(LCS(x,y))
# print(LCS_dynamo(x,y))
print(dojo_recursive(S1,S2,len(S1),len(S2)))
print(dojo_recursive(x,y,len(x),len(y)))
