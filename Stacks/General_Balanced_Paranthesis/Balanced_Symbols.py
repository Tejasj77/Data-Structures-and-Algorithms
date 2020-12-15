# Only to check if the brackets are balanced are not.
# No other symbols permitted

from Basic import Stack_ADT
expr = input()
def matches(open,close):
    lefty = '({['
    righty = ')}]'
    return lefty.index(open) == righty.index(close)

def checker(stri):
    S = Stack_ADT.Stack()
    index = 0
    balanced=True
    while index<len(expr) and balanced:
        symbol = stri[index]
        if symbol in '({[':
            S.push(symbol)
        else:
            if S.isEmpty():
                balanced=False
            else:
                top = S.pop()
                if not matches(top,symbol):
                    balanced=False
        index = index+1
    if balanced and S.isEmpty():
        return True
    else:
        return False

print(checker(expr))