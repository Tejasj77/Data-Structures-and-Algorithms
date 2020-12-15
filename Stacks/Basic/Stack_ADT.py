class Stack:
    def __init__(self):
        self.data = []
    def push(self,element):
        self.data.append(element)
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            detach = self.data[len(self.data)-1]
            self.data = self.data[0:len(self.data)-1]
            return detach
    def isEmpty(self):
        if(len(self.data)==0):
            return True
        return False
    def top(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.data[len(self.data)-1]
    def __len__(self):
        return len(self.data)
    def __iter__(self):
        return iter(self.data)
    def __str__(self):
        return str(self.data)

S = Stack()
S.push(5)
