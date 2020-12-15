#Back is the 0th element of the list and the Front is the len(dequeu)-1 th element of the list

class Deque:
    def __init__(self):
        self.queue = []
    def isEmpty(self):
        return len(self.queue)==0
    def addfront(self,element):
        self.queue.append(element)
    def addback(self,element):
        self.queue.insert(0,element)
    def removefront(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            return self.queue.pop()
    def removeback(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            temp = self.queue[0]
            self.queue = self.queue[1:]
            return temp
    def __len__(self):
        return len(self.queue)
    def __str__(self):
        return str(self.queue)

