"""
Count the no. of solution sets available inside a array that add upto a specific total value
"""
def rec(arr,total,i):
    if total<0:
        return 0
    elif total==0:
        return 1
    elif i<0:
        return 0
    elif total<arr[i]:
        return rec(arr,total,i-1)
    else:
        return rec(arr,total-arr[i],i-1)+\
               rec(arr,total,i-1)

def count_sets(arr,total):
    return rec(arr,total,len(arr)-1)

alist = [2,4,6,10]
sum = 11
print(count_sets(alist,sum))