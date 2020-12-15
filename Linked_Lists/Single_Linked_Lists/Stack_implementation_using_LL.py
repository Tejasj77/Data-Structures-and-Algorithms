class StackLL:
    class Node:
        __slots__ = 'element','next'
        def __init__(self,element):
            self.element = element
            self.next = None
        def __str__(self):
            return str(self.element)
    def __init__(self):
        self.head = None
        self.size = 0
    def isEmpty(self):
        return self.size==0
    def push(self,element):
        new_Node = self.Node(element)
        if self.isEmpty():
            self.head=new_Node
            self.tail=new_Node
        else:
            current_head = self.head
            new_Node.next = current_head
            self.head = new_Node
        self.size +=1
    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        else:
            new_head = self.head.next
            to_pop = self.head
            self.head = new_head
        self.size-=1
        return to_pop
    def __len__(self):
        return self.size
    def returnHead(self):
        return self.head
    def returnTail(self):
        return self.tail

S =StackLL()
S.push(7)
S.push(4)
S.push(1)
print(len(S))
print(S.pop())
print(len(S))
print(S.returnHead())
print(S.returnTail().next)