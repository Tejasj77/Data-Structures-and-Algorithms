# Given the array candies and the integer extraCandies,
# where candies[i] represents the number of candies that the ith kid has.
#
# For each kid check if there is a way to distribute extraCandies among the kids such that
# he or she can have the greatest number of candies among them.
# Notice that multiple kids can have the greatest number of candies.

from Hash_implementation import Hash_ADT

candies = Hash_ADT.HashTable()
inp_list = list(map(int,input().split()))

extra_candies = int(input())
max=0
for iter in inp_list:
    if(iter>max):
        max = iter              #The maximum element from the inp_list is extracted.
for iter in inp_list:           #Logic to substitute True or False in the hash table depending on the condition
    if((iter+extra_candies)>=max):
        candies.put(iter,True)
    else:
        candies.put(iter,False)

for iter in inp_list:           #Extract the boolean value from the hash table.
    print(candies.get(iter))






