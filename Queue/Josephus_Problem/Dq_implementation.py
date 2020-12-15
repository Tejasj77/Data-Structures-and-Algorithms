from collections import deque

def jospehus(ls,skip):
        dq = deque(ls)
        while len(dq)>1:
            print(dq)
            dq.rotate(-skip)
            print(dq)
            dq.pop()
        return dq.pop()

print(jospehus([1,2,3,4,5,6],2))