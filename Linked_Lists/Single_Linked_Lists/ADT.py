class Node:
    __slots__ = 'element','next'
    def __init__(self,element):
        self.element=element
        self.next=None
    def __str__(self):
        return str(self.element)

#Addition through head.
#Basic Addition only in list
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def __len__(self):
        return self.size
    def addinList(self,element):
        new_E = Node(element)
        if len(self)==0:
            self.head = new_E
            self.tail = new_E
            self.tail.next = None
        else:
            current_head = self.head
            new_E.next = current_head
            self.head=new_E
        self.size+=1
    def returnHead(self):
        return self.head
    def returnTail(self):
        return self.tail

    def removehead(self):
        if(self.size==0):
            return "Linked list is empty"
        elif(self.size==1):
            pophead = self.head
            self.head,self.tail = None,None
            self.size-=1
            return pophead.element
        else:
            pophead = self.head
            newhead = pophead.next
            self.head = newhead
            self.size-=1
            return pophead.element

# l = LinkedList()
# l.addinList(2)
# l.addinList(3)
# l.addinList(4)
# print(l.returnHead())
# print(l.returnTail())
# print("Head is removed " + str(l.removehead()))
# print(l.returnHead())
# print(l.returnTail())
# print("Head is removed " + str(l.removehead()))
# print(l.returnHead())
# print(l.returnTail())
# print("Head is removed " + str(l.removehead()))
# print(l.returnHead())
# print(l.returnTail())
# print("Head is removed " + str(l.removehead()))
# print(l.returnHead())
# print(l.returnTail())


