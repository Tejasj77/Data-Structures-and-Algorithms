def binary_search(alist,item):
    first = 0
    last= len(alist)-1

    while first<=last:
        midpoint = (first+last)//2
        if item == alist[midpoint]:
            return True
        elif item<alist[midpoint]:
            last = midpoint-1           #Exclude the midpoint because midpoint is surely not the item
        else:
            first = midpoint+1          #Exclude the midpoint because midpoint is surely not the item
    return False

sample_list = [1,3,5,7,9]
print(binary_search(sample_list,6))