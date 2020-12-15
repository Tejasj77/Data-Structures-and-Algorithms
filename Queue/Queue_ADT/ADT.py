class Queue:
    def __init__(self):
        self.data = []
    def enqueue(self,element):
        self.data.insert(0,element)
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            return self.data.pop()
    def isEmpty(self):
        if len(self.data)==0:
            return True
        return False
    def __len__(self):
        return len(self.data)
    def __str__(self):
        return str(self.data)
    def size(self):
        return len(self.data)
