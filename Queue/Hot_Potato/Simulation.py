from Queue_ADT import ADT

def hotPotato(namelist, num):
    simqueue = ADT.Queue()
    for name in namelist:
        simqueue.enqueue(name)
    print(simqueue)
    while simqueue.size() > 1:          #Revolve the Queue till only 1 element remains
        for i in range(num):                        #num is the numth element to be eliminated
            simqueue.enqueue(simqueue.dequeue())    #Move the circular queue one position at a time

        simqueue.dequeue()                          #Pop element out of the queue
        print(simqueue)
    return simqueue.dequeue()                       #Pop the last remaining element of the queue

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))
