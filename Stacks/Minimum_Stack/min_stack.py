#O(1) implementation

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
            return self.data.pop()[0]
    def minimum(self):
        return self.front()[1]
    def __len__(self):
        return len(self.data)
    def __str__(self):
        return str(self.data)
    def __iter__(self):
        return iter(self.data)

# m = MinStack()
# m.push(3)
# m.push(2)
# m.push(1)
# print(m)
# print(m.minimum())
# m.pop()
# print(m.minimum())