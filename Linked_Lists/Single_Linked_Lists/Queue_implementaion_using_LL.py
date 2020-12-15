#This implementation should be different than Stacks.
#The head of the Linked List should contain the first element of the queue.
#i.e the element which is to be dequeued, bcoz the next element can be traced through it.
#Otherwise, as tail points "None" we cannot trace the last element after popping.


class QueueLL:
    class Node:
        __slots__ = 'element','next'
        def __init__(self,element):
            self.element=element
            self.next=None
        def __str__(self):
            return f" The element is " + str(self.element)
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def isEmpty(self):
        return self.size ==0
    def enqueue(self,element):
        new_E = self.Node(element)
        if self.isEmpty():
            self.head = new_E
            self.tail = new_E
        else:
            current_tail = self.tail
            new_E.next = current_tail
            self.tail = new_E
            if self.head.next==None:
                self.head.next = self.tail
        self.size+=1
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            to_deq = self.head
            self.head = to_deq.next
            self.size-=1

        return to_deq
    def returnHead(self):
        return self.head
    def returnTail(self):
        return self.tail
Q = QueueLL()
Q.enqueue(1)
Q.enqueue(2)
Q.enqueue(3)
print(Q.returnHead())
print(Q.returnTail())
print(Q.dequeue())
print(Q.returnHead())
print(Q.returnTail())
print(Q.dequeue())
print(Q.returnHead())
print(Q.returnTail())
print(Q.dequeue())
print(Q.returnHead())
print(Q.returnTail())
print(Q.dequeue())

