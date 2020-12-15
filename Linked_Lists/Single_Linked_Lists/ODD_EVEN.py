# Given a singly linked list, group all odd nodes together followed by the even nodes.
# Please note here we are talking
# about the node number and not the value in the nodes.
#
# You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

from Single_Linked_Lists import ADT

l = ADT.LinkedList()
l.addinList(7)
l.addinList(4)
l.addinList(6)
l.addinList(5)
l.addinList(3)
l.addinList(1)
l.addinList(2)
a = ADT.LinkedList()
a.addinList(5)
a.addinList(4)
a.addinList(3)
a.addinList(2)
a.addinList(1)
#print(l.returnTail())
#print(l.returnHead())


def solution(instance):
    oddhead = instance.returnHead()

    evenhead = oddhead.next

    list1 = []

    while evenhead!=None:
        while oddhead!=None:
            list1.append(oddhead)
            if(oddhead.next==None):
                oddhead=None
            else:
                oddhead = oddhead.next.next
        list1.append(evenhead)
        if(evenhead.next==None):
            evenhead=None
        else:
            evenhead = evenhead.next.next

    for i in list1:
        print(i.element)

solution(l)
print("Break")
solution(a)