from Single_Linked_Lists import ADT

class UpdateLinkedList(ADT.LinkedList):
    def __init__(self):
        super().__init__()
    def traversing(self):
        i = 0
        current_head = self.head
        while i<self.size:
            print(current_head.element)
            i+=1
            current_head = current_head.next

L = UpdateLinkedList()

class Stack:
    def __init__(self):
        self.data = []
        self.size = 0
    def isEmpty(self):
        return self.size==0
    def push(self,element):
        self.data.insert(0,element)
        self.size+=1
    def pop(self):
        if(self.isEmpty()):
            return "Stack is Empty"
        else:
            pop_element = self.data.pop()
            self.size-=1
            return pop_element


for i in range(9,0,-1):
    L.addinList(i)
L.traversing()
print("Break")

def reverse(linked):
    """
    New Linked List will be created by reversing the previous input linked list
    A Stack is used to store the nodes and then LIFO principle to create a reverse
    :param linked:
    :return: new_linked
    """
    new_linked = UpdateLinkedList()
    starting_node = linked.returnHead()
    s = Stack()

    while starting_node!=None:
        s.push(starting_node)
        starting_node = starting_node.next

    while not s.isEmpty():
        current_element = s.pop()
        new_linked.addinList(current_element)
    return new_linked

new_reversed_linked_list = reverse(L)
#reversed_linked_list.traversing()

def traverse_reverse(linked):
    """
    Reversing the linked list while traversing through it
    :param linked:
    :return: None
    """
    current = linked.returnHead()
    linked.tail = current       #The oldhead will be the new tail
    prev = None
    while current is not None:
        second = current.next
        current.next = prev
        prev = current
        current = second
    linked.head = prev
    return linked


reversed_linked_list = traverse_reverse(L)
reversed_linked_list.traversing()
#print(fin_ans.returnHead())
#print(fin_ans.returnTail())
