from Basic import Stack_ADT

#Currently configured for integer  operation
inp_str = input()   #Add space between each element so as to split in the list.
inp_list1 = inp_str.split()

#BODMAS precedence
prec = {
    '*':3 ,
    '/':3,
    '+':2,
    '-':2 ,
    '(':1,
}

def conversion(inp_list):
    opStack = Stack_ADT.Stack()
    op_list=[]
    for iter in inp_list:
        if iter[0] in "0123456789":         #In order to classify 10,12,23,... etc. also as integers and append in output
            op_list.append(iter)
        elif iter == '(':                   #Push in the stack
            opStack.push(iter)
        elif iter ==')':
            top = opStack.pop()             #We just want to look at the top and not pop it.

            while top!='(':                 #Pop the stack till ( is encountered
                op_list.append(top)         #Append the element first otherwise if we pop it and append then ( also gets appended
                top = opStack.pop()
        else:
            while(not opStack.isEmpty())and(prec[opStack.top()]>=prec[iter]): #Pop the operators with the higher precedence first
                op_list.append(opStack.pop())
            opStack.push(iter)                                                #Then push the current operator in the stack

    while not opStack.isEmpty():
        op_list.append(opStack.pop())       # Pop the remaining operators and append in the output
    return op_list

converted = conversion(inp_list1)
print(converted)

def evaluation(list1):
    opStack = Stack_ADT.Stack()
    for iter in list1:                      # List if PostFix type
        if str(iter) in '*/+-':             # If a operator is encountered remove the top most 2 elements a
            temp_tup = [opStack.pop() for i in range(2) if not opStack.isEmpty()]   #Pop the top 2 elements
            pushback = doMath(temp_tup,iter)            # Perform the operation depending on the operator
            opStack.push(pushback)                      # Push the result back in stack for further processing.
        else:
            opStack.push(int(iter))         # If element other than operators then push the integers in the stack.
    return opStack.pop()

def doMath(tupl,i):
    if i=='*':
        return tupl[0]*tupl[1]
    elif i=='/':
        return tupl[0]/tupl[1]
    elif i=='+':
        return tupl[0]+tupl[1]
    else:
        if tupl[0]>tupl[1]:             # To add negative subtraction
            return tupl[0]-tupl[1]
        else:
            return tupl[1]-tupl[0]

print(evaluation(converted))