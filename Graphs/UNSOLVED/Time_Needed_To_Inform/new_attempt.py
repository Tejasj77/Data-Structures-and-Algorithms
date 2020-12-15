class Manager:
    def __init__(self,key,time):
        self.id = key
        self.employees = []
        self.informTime = time
    def addEmployee(self,employee):
        self.employees.append(employee)
    def __str__(self):
        return "Manager= " + str(self.id) + " Employees are " + f"{[i.id for i in self.employees]}" + " Inform Time is of " + str(self.informTime)

class Employee:
    def __init__(self,key):
        self.id = key
        self.manager = None
    def addManager(self,manager):
        self.manager = manager
    def __str__(self):
        return "Employee= " + str(self.id) + " Manager is " + str(self.manager.id)

manager = [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6]
informTime = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]
iteration = 0
for i,j in zip(manager,informTime):
    manag = Manager(i,j)
    emp = Employee(iteration)
    emp.addManager(manag)
    manag.addEmployee(emp)

    print(manag)
    print(emp)
    iteration+=1
