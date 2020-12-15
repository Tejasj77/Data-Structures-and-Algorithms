from Double_Ended_Queue import Deq_ADT

inp_str = input()

def palcheck(stri):
    d = Deq_ADT.Deque()
    for i in stri:
        d.addfront(i)

    while len(d)>1:
        fro = d.removefront()
        re = d.removeback()
        if(fro!=re):
            return False
    return True

print(palcheck(inp_str))

