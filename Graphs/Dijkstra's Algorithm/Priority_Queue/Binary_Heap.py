class BinHeap:
    def __init__(self):
        self.heaplist = [0]
        self.currentsize = 0
    def percUp(self,i):
        while i//2 >0:
            if self.heaplist[i]<self.heaplist[i//2]:
                self.heaplist[i],self.heaplist[i//2] = self.heaplist[i//2],self.heaplist[i]
                # tmp = self.heaplist[i//2]
                # self.heaplist[i//2] = self.heaplist[i]
                # self.heaplist[i] = tmp
            i = i//2
    def insert(self,k):
        self.heaplist.append(k)
        self.currentsize = self.currentsize+1
        self.percUp(self.currentsize)

    def minchild(self,i):
        if(i*2+1)>self.currentsize:
            return i*2
        else:
            if(self.heaplist[i*2]<self.heaplist[i*2+1]):
                return i*2
            else:
                return i*2+1
    def percDown(self,i):
        while(i*2)<=self.currentsize:
            mc=self.minchild(i)
            if(self.heaplist[i]>self.heaplist[mc]):
                self.heaplist[i],self.heaplist[mc] = self.heaplist[mc],self.heaplist[i]
                # tmp = self.heaplist[i]
                # self.heaplist[i] = self.heaplist[mc]
                # self.heaplist[mc] = tmp
            i=mc
    def delMin(self):
        rootval = self.heaplist[1]
        self.heaplist[1] = self.heaplist[self.currentsize]
        self.currentsize=self.currentsize+1
        self.heaplist.pop()
        self.percDown(1)
        return rootval
    def __str__(self):
        return f"{self.heaplist}"

b = BinHeap()
b.insert(1)
b.insert(4)
b.insert(2)
b.insert(3)
b.insert(5)
print(b)