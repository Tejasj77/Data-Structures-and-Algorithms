"""
Using dictionary to store the sums of subsets.
"""
def rec(arr,total,i,mem):
    key = str(total) + ';' + str(i)
    if key in mem:
        return mem[key]
    if total<0:
        return 0
    elif total == 0:
        return 1

    elif i<0:
        return 0
    elif total<arr[i]:
        result =  rec(arr,total,i-1,mem)
    else:
        result  = rec(arr,total-arr[i],i-1,mem) + \
                  rec(arr,total,i-1,mem)
    mem[key] = result
    return result
def count_sets(arr,total):
    mem = {}
    return rec(arr,total,len(arr)-1,mem)

arrlist = [2,4,6,10]
sum = 22
print(count_sets(arrlist,sum))