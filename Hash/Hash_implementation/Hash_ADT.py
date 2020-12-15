class HashTable:
    def __init__(self):
        self.size = 11                          #Arbitrary Prime number for Collision Resolution Algo.
        self.slots = [None] * self.size         #List containing the keys to the actual data
        self.data = [None] * self.size          #Actual data

    def hash_function(self,key,size):
        return key%size                         #Return the hash position using the remainder method
    def rehash(self,oldhash,size):
        return (oldhash+1)%size                 #Linear probing i.e checking in the next slot

    def put(self,key,value):
        hash_value = self.hash_function(key,len(self.slots))

        if self.slots[hash_value] is None:      #The hash position is Empty. Thus, we can add
            self.slots[hash_value] = key
            self.data[hash_value] = value
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = value  #replace
            else:                               #Not Empty
                next_slot = self.rehash(hash_value,len(self.slots))
                while(self.slots[next_slot] is not None and self.slots[next_slot]!=key):
                    # Continue rehashing till empty slot is found
                    next_slot = self.rehash(next_slot, len(self.slots))

                if self.slots[next_slot] is None: #The hash position is Empty. Thus, we can add
                    self.slots[next_slot] = key
                    self.data[next_slot] = value
                else:
                    self.data[next_slot] = value  #replace

    def get(self,key):
        start_slot = self.hash_function(key,len(self.slots))
        position = start_slot                   #Storing the initial position

        while self.slots[position] is not None: #Element is present
            if self.slots[position] == key:     #Hash value is found
                return self.data[position]      #Return the actual data value
            else:
                position = self.rehash(position,len(self.slots))    #Linear probing i.e the next slot.
                if(position == start_slot):     #We have reached the initial position and thus, element is absent
                    return None

    def __getitem__(self, item):
        self.get(item)
    def __setitem__(self, key, value):
        self.put(key,value)


