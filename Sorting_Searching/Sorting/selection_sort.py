"""
Iterate through the list and compare with all the next values in the list.
Swap the current element with the last index
"""

def selection_sort(alist):
    for i,item in enumerate(alist):
        min_idx = len(alist)-1              #The pointer to the last element.
        for j in range(i,len(alist)):
            """
            After this for loop, the "min_idx" is index such that the immediate next great element is selected.
            """
            if alist[j]<alist[min_idx]:     #The jth element is less than the last element.
                min_idx = j                 #Store the jth index in the "min_idx"
        if min_idx!=i:                      #The next greater element is not the same as the current element.
            alist[min_idx],alist[i] = alist[i],alist[min_idx]

sample = [1,5,9,8,2,3,4]
selection_sort(sample)
print(sample)