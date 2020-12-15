"""
def quick_sort(a_list):
    quick_sort_helper(a_list, 0, len(a_list) - 1)

def quick_sort_helper(a_list, first, last):
    print(a_list)
    if first < last:
        split = partition(a_list, first, last)
        print(split,first,last)
        quick_sort_helper(a_list, first, split - 1)
        quick_sort_helper(a_list, split + 1, last)

def partition(a_list, first, last):
    pivot_val = a_list[first]
    left_mark = first + 1
    right_mark = last
    done = False

    while not done:
        while left_mark <= right_mark and a_list[left_mark] <= pivot_val:
            left_mark = left_mark + 1
        while left_mark <= right_mark and a_list[right_mark] >= pivot_val:
            right_mark = right_mark - 1
        if right_mark < left_mark:
            done = True
        else:
            a_list[left_mark], a_list[right_mark] = (
                a_list[right_mark],
                a_list[left_mark],
            )
    a_list[first], a_list[right_mark] = a_list[right_mark], a_list[first]

    return right_mark


a_list = [54,11,26,44,23,13,31,22]
quick_sort(a_list)
print(a_list)

"""
inp_list = [15,5,7,20,2,10]

def partition(list1,low,high):
    i = low-1
    pivot = list1[high]

    for j in range(low,high):
        if list1[j]<pivot:
            i=i+1
            list1[i],list1[j] = list1[j],list1[i]
    list1[high],list1[i+1] = list1[i+1],list1[high]
    return i+1

def quick_sort(list1,low,high):
    if low<high:
        pi = partition(list1,low,high)
        print(list1[low:pi-1],list1[pi+1:high])
        quick_sort(list1,low,pi-1)
        quick_sort(list1,pi+1,high)
        return list1

sorted_list = quick_sort(inp_list,0,len(inp_list)-1)
print(sorted_list)
