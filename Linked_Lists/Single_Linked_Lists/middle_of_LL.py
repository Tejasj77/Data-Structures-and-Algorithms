from Single_Linked_Lists import ADT

L = ADT.LinkedList()
for iter in range(10,0,-1):
    L.addinList(iter)
print(L.returnHead(),L.returnTail(),L.size)

def naive_middle(lilist):
    """
    Finding the half index of the list by dividing the size and then traversing to it.
    :param lilist:
    :return: middle_element
    """

    length = lilist.size
    terminate_at = int(length/2)
    start = lilist.returnHead()
    iter=1                      #bcoz size starts from 1.

    while iter!=terminate_at:
        start = start.next
        iter += 1

    return start.element

def clever_middle(lilist):
    """
    Using two pointers one fast and slow. fast jumps 2 steps and slow jumps 1 step.
    when fast reached end of Linked list then slow reaches the middle of the list.
    :param lilist:
    :return: middle_element
    """

    head = lilist.returnHead()
    fast_pointer,slow_pointer = head,head
    while fast_pointer.next!=None and fast_pointer.next.next!=None:

        fast_pointer = fast_pointer.next.next
        slow_pointer = slow_pointer.next

    return slow_pointer.element

print(naive_middle(L))
print(clever_middle(L))