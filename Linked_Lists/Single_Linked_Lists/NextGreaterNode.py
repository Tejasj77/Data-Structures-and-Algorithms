# We are given a linked list with head as the first node.
# Let's number the nodes in the list: node_1, node_2, node_3, ... etc.
#
# Each node may have a next larger value: for node_i, next_larger(node_i) is the node_j.val such that j > i, node_j.val > node_i.val,
# and j is the smallest possible choice.  If such a j does not exist, the next larger value is 0.
#
# Return an array of integers answer, where answer[i] = next_larger(node_{i+1}).
#
# Note that in the example inputs (not outputs) below, arrays such as [2,1,5] represent the serialization
# of a linked list with a head node value of 2, second node value of 1, and third node value of 5.
import sys
from Single_Linked_Lists import ADT

l = ADT.LinkedList()
l.addinList(1)
l.addinList(5)
l.addinList(2)
l.addinList(9)
l.addinList(1)
l.addinList(5)
l.addinList(7)
l.addinList(1)

print(l.returnHead())
def solution(instance):
    head = instance.returnHead()
    list1 = [0]*len(l)
    iter  = 0

    while head!=None:
        start = head
        max = 0
        while start.next!=None:
            if(head.element<start.next.element):
                max =start.next.element
                break
            start = start.next

        if(max!=sys.maxsize):
            list1[iter] = max
        iter += 1
        head = head.next

    return list1

ans = solution(l)
print(ans)