#Floyd Cycle-Finding Algorithm

from Double_Linked_Lists import Double_LL

class Update_Double_Linked_List(Double_LL.Double_LL):
    def __init__(self):
        super().__init__()
    def returnFirst(self):
        return self.header.next


def traversing_LL(lilist):
    head = lilist.returnFirst()
    tortoise,hare = head,head

    while hare.next!=None and hare.next.next!=None and tortoise.next!=None:
        tortoise = tortoise.next    #1 hop
        hare = hare.next.next       #2 hop
        #Loop Detected
        if(tortoise==hare):
            return True

    return False

D = Update_Double_Linked_List()
D.insertBetween(1)
D.insertBetween(2,1,None)

D.insertBetween(3,2,None)
D.insertBetween(4,3,None)
D.insertBetween(5,4,1)
print(traversing_LL(D))








