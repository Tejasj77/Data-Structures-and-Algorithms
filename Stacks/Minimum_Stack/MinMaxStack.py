#O(1) implementation of Min Max Stack operations in the Same ADT


class MinMaxStack:
    def __init__(self):
        self.data = []
    def isEmpty(self):
        return len(self.data)==0
    def front(self):
        return self.data[len(self.data)-1]
    def push(self,element):
        if self.isEmpty():
            self.data.append((element,element,element))
        elif self.front()[1]<element<self.front()[2]:
            self.data.append((element,self.front()[1],self.front()[2]))
        elif element<self.front()[1]:
            self.data.append((element,element,self.front()[2]))
        elif element>self.front()[2]:
            self.data.append((element,self.front()[1],element))
    def pop(self):
        self.data.pop()
    def maximum(self):
        return self.front()[2]
    def minimum(self):
        return self.front()[1]
    def __str__(self):
        return str(self.data)
    def __iter__(self):
        return iter(self.data)


T = MinMaxStack()
T.push(20)
T.push(10)
T.push(40)
T.push(100)
T.push(50)
print(T)
print(T.maximum())
print(T.minimum())
T.pop()
T.pop()
print(T.maximum())