class BinaryHeap:
    def __init__(self):
        self.heap = []
        self.size = 0
    def percUp(self,current):
        """
        This method moves the added node from the bottom of the tree (end of the list)
        to it's appropriate position
        :param current:
        :return:
        """
        while (current-1)//2>=0:                        #Checking if parent index i.e. parent node exists
            parent = (current-1)//2
            if self.heap[parent]>self.heap[current]:    #If parent node > child node => exchange positions
                self.heap[parent],self.heap[current] = self.heap[current],self.heap[parent]
            current = parent                            #Move up the tree

    def insert(self,element):
        self.heap.append(element)                       #Node is added at the end of the heap.
        self.size +=1
        self.percUp(len(self.heap)-1)                   #The added node is moved in the proper position in the graph

    def percDown(self,current):
        """
        This method moves the root node from the top of the tree(0th index of the list)
         to it's appropriate position in the list
        :param current:
        :return:
        """
        while (2*current+1)<len(self.heap):             #Checking if left child index exists bcoz left child is added first.
            min_child = self.getmin(current)            #Storing the minimum among the child nodes.
            if self.heap[current] > self.heap[min_child]:
                #Exchanging place if the child is less than the parent.
                self.heap[current],self.heap[min_child] = self.heap[min_child],self.heap[current]
            else:
                return
            current = min_child                         #Move to the child node.
    def getmin(self,parent):
        """
        Returns minimum node among the child nodes.
        :param parent:
        :return: The minimum of the child nodes
        """
        if 2*parent+2>(len(self.heap)-1):               #If right child does not exist
            return 2*parent+1                           #Return left child index.
        if self.heap[2*parent+1]<self.heap[2*parent+2]: #Check if left child < right child
            return 2*parent+1                           #Return left child index
        return 2*parent+2                               #Else : Return right child index

    def delete(self):
        """
        Delete or extract the minimum node from the heap i.e. the root of the tree.
        :return:
        """
        self.heap[0],self.heap[-1] = self.heap[-1],self.heap[0]     #Exchange the 0th index with the last element of heap
        result = self.heap.pop()                                    #Pop the new last element
        self.percDown(0)                                            #Rearrange the heap according to the heap property
        return result

    def heapify(self,not_a_heap):
        self.heap = not_a_heap[:]
        current = len(self.heap)//2 -1
        while current>=0:
            self.percDown(current)
            current-=1

h = BinaryHeap()
# h.insert(50)
# h.insert(20)
# h.insert(10)
# print(h.delete())
# print(h.delete())

sample = [50,10,20,30]
h.heapify(sample)
for _ in range(len(sample)):
    print(h.delete())