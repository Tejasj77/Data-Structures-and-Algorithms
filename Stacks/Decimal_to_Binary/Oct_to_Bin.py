from Basic import Stack_ADT
decimal = int(input())
S = Stack_ADT.Stack()
number=decimal
counter=0
while int(number)>0:
    counter+=1
    print(number)
    rem = number%8
    print(rem)
    number = number/8
    S.push(int(rem))

result = []
for i in range(counter):
    result.append(S.pop())

fin = ''
for i in result:
    fin+=str(i)
print(fin)