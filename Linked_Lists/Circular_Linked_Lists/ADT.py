class CircularLL:
    class Node:
        __slots__ = 'element','next'
        def __init__(self,element):
            self.element = element
            self.next = None
        def __str__(self):
            return str(self.element)

    def __init__(self):
        self.tail = None
        self.size = 0
    def isEmpty(self):
        return self.size==0
    def front(self):
        if(self.isEmpty()):
            return "Linked List is Empty"
        else:
            head = self.tail.next
            return head.element
    def dequeue(self):
        #Delete from the head position
        #we get new head
        if(self.isEmpty()):
            return "Linked List is Empty"
        else:
            oldhead = self.tail.next
            if(self.size==1):
                self.tail = None
            else:
                self.tail.next = oldhead.next
        self.size-=1
        return oldhead.element
    def enqueue(self,element):
        #Insert between the head and the tail position
        #New Tail
        new_E = self.Node(element)
        if(self.isEmpty()):
            #circular initialisation
            new_E.next = new_E
        else:
            new_E.next = self.tail.next
            self.tail.next = new_E
        self.tail = new_E
        self.size+=1
    def returnTail(self):
        return self.tail.element
    def rotate(self):
        if(self.size>0):
            self.tail = self.tail.next

# l = CircularLL()
# l.enqueue(3)
# print("The tail is "+ str(l.returnTail()))
# print("The head is %d" % l.front())
# l.enqueue(5)
# print("The tail is "+ str(l.returnTail()))
# print("The head is %d" % l.front())
# l.enqueue(8)
# print("The tail is "+ str(l.returnTail()))
# print("The head is %d" % l.front())
# l.rotate()
# print("The tail is "+ str(l.returnTail()))
# print("The head is %d" % l.front())
