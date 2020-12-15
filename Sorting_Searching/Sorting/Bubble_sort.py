"""
Iterate and compare with next value only.
This leads to the bubbling of the largest value to the end of the list during one iteration.
In the next iteration, the second largest value is bubbled to the last.
So on and so forth...
"""

def Bubble_Sort(alist):
    size = len(alist)-1         #As we are using "iter+1" in the logic below, we are restricting the size to length-1
    unsorted = False
    while unsorted ==False:
        unsorted = True                     #Sorting is completed and exit the while loop
        for iter in range(size):
            if alist[iter]>alist[iter+1]:   #The element before the next element is greater indicating list is unsorted
                unsorted=False              #As list is unsorted
                alist[iter],alist[iter+1] = alist[iter+1],alist[iter]   #Place Swapping

sample = [1,5,6,4,8,2,3,9]
Bubble_Sort(sample)
print(sample)