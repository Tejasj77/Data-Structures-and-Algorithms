class MinStack:
    def __init__(self):
        self.data = []
    def isEmpty(self):
        return len(self.data)==0
    def front(self):
        return self.data[len(self.data)-1]
    def push(self,element):
        if(self.isEmpty() or element<self.front()[1]):
            self.data.append((element, element))
        else:
            self.data.append((element, self.front()[1]))

    def pop(self):
        if(self.isEmpty()):
            return "Stack is Empty"
        else:
            return self.data.pop()
    def minimum(self):
        return self.front()[1]
    def __len__(self):
        return len(self.data)
    def __str__(self):
        return str(self.data)
    def __iter__(self):
        return iter(self.data)

class MinQueue:
    def __init__(self):
        self.s1 = MinStack()
        self.s2 = MinStack()
        self.size = 0
    def isEmpty(self):
        return self.s1.isEmpty() and self.s2.isEmpty()
    def enqueue(self,element):
        self.s1.push(element)
    def minimum(self):
        if(self.s1.isEmpty() or self.s2.isEmpty()):
            if(self.s1.isEmpty()):
                return self.s2.minimum()
            else:
                return self.s1.minimum()
        else:
            if(self.s1.minimum()<self.s2.minimum()):
                return self.s1.minimum()
            return self.s2.minimum()
    def dequeue(self):
        if(self.s2.isEmpty()):
            while(not self.s1.isEmpty()):
                temp =  self.s1.pop()
                #print(temp[0])
                self.s2.push(temp[0])
        return self.s2.pop()
    def __iter__(self):
        return iter(zip(self.s1,self.s2))

q = MinQueue()
q.enqueue(25)
q.enqueue(32)
q.enqueue(100)
q.enqueue(40)
q.enqueue(10)
q.enqueue(125)
print(q.minimum())
q.dequeue()
print(q.minimum())
q.dequeue()
print(q.minimum())
q.dequeue()





