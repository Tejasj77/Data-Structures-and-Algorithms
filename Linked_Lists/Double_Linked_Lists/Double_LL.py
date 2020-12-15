class Node:
    __slots__ = 'element','next','prev'
    def __init__(self,e):
        self.element=e
        self.prev=None
        self.next=None
    def __str__(self):
        return f"The element is " + str(self.element)

class Double_LL:
    def __init__(self):
        self.header = Node("head")
        self.trailer = Node("tail")
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size=0
    def isEmpty(self):
        return self.size==0
    def addNode(self,e):
        newNode = Node(e)
        return newNode
    def getNode(self,e):
        getter = self.header
        while getter.element!=e:
            getter = getter.next
        if getter.element==self.header.element:
            return False
        return getter

    def insertBetween(self,e,predecessor=None,successor=None):
        new_E = self.addNode(e)

        if(self.isEmpty()):
            self.header.next = new_E
            self.trailer.prev = new_E
            new_E.next = self.trailer
            new_E.prev = self.header
            self.size+=1
        else:
            if predecessor!=None:
                try:
                    if self.getNode(predecessor):
                        #If the predecessor already exists in the Linked List, use that
                        print("Predecessor exists")
                        self.pred = self.getNode(predecessor)
                except AttributeError:
                    #If the predecessor does not exist already in the Linked List, add it as a Node
                    self.pred = self.addNode(predecessor)
                    self.size+=1
                #If we are inserting between trailer node and predecessor node, sever the connection between them
                if(self.trailer.prev==self.pred):
                    self.trailer.prev = new_E
                #Establish connections
                new_E.prev = self.pred
                self.pred.next = new_E
            else:
                #If predecessor is None this means we are adding the first element in the Linked List
                new_E.prev = self.header
            if successor!=None:
                try:
                    if self.getNode(successor):
                        # If the successor already exists in the Linked List, use that
                        print("Successor exists")
                        self.succ = self.getNode(successor)
                except AttributeError:
                    # If the successor does not exist already in the Linked List, add it as a Node
                    self.succ = self.addNode(successor)
                    self.size+=1
                # If we are inserting between header node and successor node, sever the connection between them
                if(self.header.next==self.succ):
                    self.header.next = new_E
                # Establish connections
                new_E.next = self.succ
                self.succ.prev = new_E
            else:
                # If successor is None this means we are adding the first element in the Linked List
                new_E.next = self.trailer
        self.size += 1
        return new_E

    def deleteNode(self,e):
        node = self.getNode(e)
        predecessor = node.prev
        successor = node.next
        predecessor.next = successor
        successor.prev = predecessor
        element = node.element
        node.prev = node.next = node = None
        return element
    def traversing(self):
        print("The head is " + str(self.header))
        start = self.header.next
        while start!=None:
            print(start)
            start = start.next



#
# d = Double_LL()
# d.insertBetween(0)
# #print(d.traversing())
# d.insertBetween(1,0)
# #print(d.traversing())
# #print(d.getNode(0).next)
# d.insertBetween(0.5,0,1)
# ans = d.getNode(0.5)
# #print(ans.prev,ans,ans.next)
# #print(d.traversing())
# d.insertBetween(0.7,0.5,1)
# #print(d.traversing())
# print(d.deleteNode(0.7))
# #print(d.traversing())
# print(d.deleteNode(0))
# print(d.getNode(0.5).prev)
# #print(d.traversing())