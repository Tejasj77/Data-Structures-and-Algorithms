def countWaysUtil(x,n,num,storage):
    #print((x,n,num))
    val = (x-pow(num,n))
    #print(val)
    if val==0:
        storage.append((x,n,num))
        print(storage)
        return 1
    if val<0:
        return 0
    return countWaysUtil(val,n,num+1,storage) + countWaysUtil(x,n,num+1,storage)

def countWays(x,n):
    return countWaysUtil(x,n,1,[])

print(countWays(100,2))