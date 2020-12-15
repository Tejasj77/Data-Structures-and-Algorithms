def rec_binary_search(alist,item):
    if len(alist)==0:
        return False
    midpoint = len(alist)//2
    if alist[midpoint]==item:
        return True
    elif item<alist[midpoint]:
        return rec_binary_search(alist[:midpoint],item)
    else:
        return rec_binary_search(alist[midpoint+1:],item)


sample = [1,3,5,7,9]
print(rec_binary_search(sample,10))