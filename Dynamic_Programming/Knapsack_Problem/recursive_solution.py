value = [None,60,100,120]
wt = [None,10,20,30]
W = 50

def knap(n,w):
    if n==0 or w==0:
        return 0
    elif wt[n] > w:
        return knap(n-1,w)
    else:
        tmp1 = knap(n-1,w)
        tmp2 = value[n] + knap(n-1,w-wt[n])
        return max(tmp1,tmp2)
print(knap(3,W))
