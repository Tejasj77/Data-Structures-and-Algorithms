"""
Iterate and compare with all previous values in the list and swap accordingly.
"""

def insertion_sort(alist):
    for i in range(1,len(alist)):
        key = alist[i]
        j = i-1

        while j>-1 and alist[j]>key:
            alist[j+1] = alist[j]
            j=j-1
        alist[j+1] = key

sample = [1,6,4,2,8,9,7]
insertion_sort(sample)
print(sample)