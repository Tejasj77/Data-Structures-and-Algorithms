from Double_Linked_Lists import Double_LL

class Deque(Double_LL.Double_LL):
    def __init__(self):
        super().__init__()
        self.len=0

    def front(self):
        if(not self.isEmpty()):
            return self.header.next.element
        return "Deque is empty"
    def back(self):
        if (not self.isEmpty()):
            return self.trailer.prev.element
        return "Deque is empty"
    def addfront(self,e):
        newelement = self.addNode(e)
        oldhead = self.header.next
        oldhead.prev = newelement
        self.header.next = newelement
        newelement.next = oldhead
        newelement.prev = self.header
        self.len+=1
    def addback(self,e):
        newelement = self.addNode(e)
        oldtail = self.trailer.prev
        oldtail.next = newelement
        self.trailer.prev = newelement
        newelement.next = self.trailer
        newelement.prev = oldtail
        self.len+=1
    def removefront(self):
        pophead = self.header.next
        newhead = pophead.next
        self.header.next = newhead
        newhead.prev = self.header
        self.len-=1
        return pophead.element

    def removeback(self):
        poptail = self.trailer.prev
        newtail = poptail.prev
        self.trailer.prev = newtail
        newtail.next = self.trailer
        self.len -= 1
        return poptail.element


D = Deque()
D.addfront(1)
D.addback(3)
D.addback(5)
D.addfront(0.1)
print(D.traversing())
print(D.removefront())
print(D.removeback())
print(D.traversing())

