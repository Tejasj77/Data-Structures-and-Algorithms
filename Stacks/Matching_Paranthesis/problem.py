from Basic import Stack_ADT
lefty = '{[('
righty = '}])'
str = input()
S = Stack_ADT.Stack()
flag=True
for iter in str:
    if iter in lefty:
        S.push(iter)
for iter in str:
    if iter in righty:
        if S.isEmpty():
            flag=False
        S.pop()

if S.isEmpty() and flag==True:
    print("Paranthesis have matched")
else:
    print("Dude,wtf")