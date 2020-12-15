from Single_Linked_Lists import ADT

L = ADT.LinkedList()
l = ADT.LinkedList()

for iter in range(5,0,-1):
    L.addinList(iter)

for iter in range(0,3):
    l.addinList(iter)

print(L.returnHead(),L.returnTail())
print(l.returnHead(),l.returnTail())

def traversing(a,b):
    head_a = a.returnHead()
    head_b = b.returnHead()

    while head_a.next!=None and head_a!=head_b:         #Before exhausting A Linked List
        while head_b.next!=None and head_a!=head_b:     #Before exhausting B Linked List
            head_b = head_b.next
            if(head_a.element==head_b.element):         #If equal return intersection point
                return head_a
        head_a=head_a.next

print(traversing(L,l))
