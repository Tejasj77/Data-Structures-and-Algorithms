value = [60,100,120]
wt = [10,20,30]
W = 50
size = len(wt)

table = [[-1 for i in range(W+1)] for j in range(size+1)]

def knap(n,w):
    if table[n][w] != -1:
        return table[n][w]
    if n==0 or w==0:
        result =  0
    elif wt[n-1]>w:
        result = knap(n-1,w)
    else:
        tmp1 = knap(n-1,w)
        tmp2 = value[n-1] + knap(n-1,w-wt[n-1])
        result = max(tmp1,tmp2)
    table[n][w] = result
    return result
print(knap(size,W))