import random as rd
class Task:
    def __init__(self,time,bool):
        self.time = time
        self.pages = rd.randint(1,5)
        if bool==1:
            self.color = True
        else:
            self.color = False


    def __str__(self):
        return str(self.time) + " with color " + str(self.color)

class Printer:
    def __init__(self):
        self.queue = []
        self.currentTask = None
        self.extime = 0
        self.tottime = []
        self.tracker = []
    def enqueue(self,element):
        self.tracker.append(element)
        self.queue.insert(0,element)
    def dequeue(self):
        if not self.isbusy():
            return "Queue is empty"
        else:
            return self.queue.pop()
    def isbusy(self):
        if len(self.queue)==0:
            return False
        else:
            return True
    def execute_queue(self):
        while self.isbusy():
            execute = self.dequeue()
            self.extime += (execute.time) + ((execute.pages) * (10 if execute.color != 0 else 5))
            self.tottime.append(self.extime)

    def send_print(self,job):
        self.enqueue(job)
        self.execute_queue()

    def totalprinttime(self):
        sum = 0
        for i in self.tottime:
            sum +=i
        return sum
    def __len__(self):
        return len(self.queue)
    def __str__(self):
        return str(self.queue)
    def __iter__(self):
        return iter(self.tracker)

p = Printer()
for i in range(1,99):
    if(i%10==0):
        j = rd.randrange(0,2)
        t = Task(i,j)
        p.send_print(t)

for i in p:
    print(i)

print(p.tottime)
print(p.totalprinttime())
