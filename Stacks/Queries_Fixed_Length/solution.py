#https://www.hackerrank.com/challenges/queries-with-fixed-length/problem
from Minimum_Stack import min_stack

class MaxStack:
    def __init__(self):
        self.data = []
    def isEmpty(self):
        return len(self.data)==0
    def push(self,element):
        if(self.isEmpty()):
            self.data.append((element,element))
        elif(element>self.maximum()):
            self.data.append((element,element))
        else:
            self.data.append((element,self.maximum()))
    def front(self):
        return self.data[len(self.data)-1]
    def maximum(self):
        return self.front()[1]
    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        else:
            return self.data.pop()
    def __iter__(self):
        return iter(self.data)
    def __len__(self):
        return len(self.data)
    def __str__(self):
        return str(self.data)


inp_list = list(map(int,input().split()))
print(inp_list)
query_list = [869
,886
,521
,646
,288
,251
,119
,285
,714
,460
,390
,704
,640
,779
,667
,754
,312
,812
,50
,7
,974
,339
,101
,253
,86
,204
,864
,439
,732
,649
,436
,646
,645
,243
,220
,706
,730
,425
,218
,730
,172
,507
,104
,61
,542
,582
,510
,853
,960
,365
,743
,107
,438
,296
,669
,522
,914
,923
,372
,988
,175
,647
,320
,258
,103
,369
,522
,536
,892
,795
,986
,39
,667
,795
,847
,986
,494
,273
,376
,88
,713
,471
,361
,917
,108
,325
,206
,497
,569
,744
,355
,176
,878
,753
,165]

def simulate2(iterator):
    tot_list = []
    j = 0
    print(f"Push in a single stack with counter = {iterator}")
    minS = min_stack.MinStack()
    while j+iterator<len(inp_list)+1:
        maxS = MaxStack()
        for iter in range(j,j+iterator):
            maxS.push(inp_list[iter])
        tot_list.append(maxS.maximum())
        j+=1
    for maxs in tot_list:
        minS.push(maxs)
    print(minS.minimum())


def simulate1(list1,list2):
    for i in list2:
        simulate2(i)

simulate1(inp_list,query_list)



