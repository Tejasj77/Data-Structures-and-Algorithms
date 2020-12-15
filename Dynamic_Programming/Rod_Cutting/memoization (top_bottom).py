rod_length = 4
price = [1,5,8,9]
r = [-1]*(rod_length+1)

def cut_rod(p,n):
    if r[n]>=0:
        return r[n]
    if n==0:
        return 0
    else:
        q=-1
        for i in range(1,n+1):
            q = max(q,p[i]+cut_rod(p,n-i))
            r[n]=q
        return q
print(cut_rod(price,rod_length))