"""
Divide and Conquer
"""
def merge_sort(alist):
    print("Splitting", alist)
    if len(alist)>1:
        mid = len(alist)//2
        left_list = alist[:mid]
        right_list = alist[mid:]
        merge_sort(left_list)
        merge_sort(right_list)
        i,j,k = 0,0,0

        while i<len(left_list) and j<len(right_list):
            if left_list[i] < right_list[j]:
                alist[k] = left_list[i]
                i = i+1
            else:
                alist[k] = right_list[j]
                j = j+1
            k = k+1

        while(i<len(left_list)):
            alist[k] = left_list[i]
            i = i+1
            k = k+1
        while(j<len(right_list)):
            alist[k] = right_list[j]
            j = j+1
            k = k+1
        print("Merging", alist)

sample = [9,8,7,5,4,3,2,1]
merge_sort(sample)
print("Sorted list is" , sample)
