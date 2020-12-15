#Circular queue
#O(1) implementation
#Front pointer is the 0th element in the list which indicates the mouth of the queue is the beginning of the list.


class Queue:
    def __init__(self):
        self.data =[None]*2
        self.front = 0
        self.size=0

    def __len__(self):
        return self.size

    def isempty(self):
        return self.size==0

    def first(self):
        if self.isempty():
            return "Queue is empty"
        else:
            return self.data[self.front]

    def resize(self,new_size):
        old=self.data
        self.data=[None]*new_size
        walk = self.front
        for k in range(self.size):
            self.data[k] = old[walk]
            walk = (walk+1)%len(old)
            print(walk)
        self.front=0


    def enqueue(self,e):
        if self.size==len(self.data):
            self.resize(2*len(self.data))

        f = (self.front+self.size)%len(self.data)
        print(f)
        self.data[f] = e
        self.size+=1

    def dequeu(self):
        answer = self.data[self.front]
        self.data[self.front] = None
        self.front=(self.front+1)%len(self.data)
        self.size-=1
        return answer
    def __str__(self):
        return str(self.data)

Q = Queue()
Q.enqueue(3)
Q.enqueue(6)
print(Q)
Q.enqueue(7)
print(Q)
print(Q.dequeu())

