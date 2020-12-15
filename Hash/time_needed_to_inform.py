from Hash_implementation import Hash_ADT

# class Employee:
#     def __init__(self,number,manager,time):
#         self.name = number
#         self.manager = manager
#         self.informTime = time
#     def __str__(self):
#         return str(self.name) + " Manager " + str(self.manager) + " Time " + str(self.informTime)

class Manager:
    def __init__(self,number,time):
        self.name = number
        self.employees = []
        self.informTime = time
    def addEmployee(self,employee):
        self.employees.append(employee)
    def __str__(self):
        return str(self.name) + " Handling " + f"{[i for i in self.employees]}" + " Time " + str(self.informTime)

#manager = [1,2,3,4,5,6,-1]
#informTime = [0,6,5,4,3,2,1]
#manager = [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6]

#informTime = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]

manager = [-1,5,0,6,7,0,0,0]
informTime = [89,0,0,0,0,523,241,519]

iter=0
emp_list = Hash_ADT.HashTable()
manager_list = Hash_ADT.HashTable()
#level=0
for i,j in zip(manager,informTime):
    #emp_list.put(iter,Employee(iter,i,j))
    m = manager_list.get(i)
    if m!=None:
        m.addEmployee(iter)
        manager_list.put(i,m)
    else:
        m_inst = Manager(i, j)
        m_inst.addEmployee(iter)
        manager_list.put(i, m_inst)
    iter += 1

#print("And the CEO is " + str(emp_list.get(6)))
print("And the CEO is " + str(manager_list.get(-1)))
start = manager_list.get(-1)
total = 0
while start!=None:
    if(start.informTime==0):
        start=None
    else:
        print(start.employees)
        for i in start.employees:
            total += start.informTime
            start = manager_list.get(i)
            break

#print(total)
print(level)

# for i in manager_list.data:
#     print(i)
