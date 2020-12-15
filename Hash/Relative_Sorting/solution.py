# Given two arrays A1[] and A2[] of size N and M respectively.
# The task is to sort A1 in such a way that the relative order among the elements will be same as those in A2.
# For the elements not present in A2, append them at last in sorted order.
# It is also given that the number of elements in A2[] are smaller than
# or equal to number of elements in A1[] and A2[] has all distinct elements.


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
                self.slots[hash_value] = value  #replace
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

    # def __getitem__(self, item):
    #     self.get(item)
    # def __setitem__(self, key, value):
    #     self.put(key,value)


freq = HashTable()

first = [5, 8, 9, 3, 5, 7, 1, 3, 4, 9, 3, 5, 1, 8, 4]
second = [3, 5, 7, 2]

def customSort(first, second):

    # dict to store frequency of each element of first list
    freq = {}

    # freq frequency of each element of first list and
    # store it in a dict.
    for i in first:
        freq[i] = freq.get(i, 0) + 1

    # Note that once we have the frequencies of all elements of
    # first list, we can overwrite elements of first list

    index = 0

    # do for every element of second list
    for i in second:

        # If current element is present in the dictionary, print it n times
        # where n is the frequency of that element in first list
        n = freq.setdefault(i, 0)
        for _ in range(n):
            first[index] = i
            index = index + 1

        # erase the element from dict
        freq.pop(i)

    # Now we are only left with elements that are only present
    # in the first list but present not in the second list
    # We need to sort the remaining elements present in the dictionary
    for key in sorted(freq.keys()):
        count = freq.get(key)
        while count:
            first[index] = key
            count = count - 1
            index = index + 1

customSort(first,second)

print(first)