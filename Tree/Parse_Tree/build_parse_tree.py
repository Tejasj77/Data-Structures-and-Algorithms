#Equation
#((3+4)*7)

class BinaryTree:
    def __init__(self,root):
        self.root = root
        self.left_child = None
        self.right_child = None
    def insert_left(self,newchild):
        newest = BinaryTree(newchild)
        if self.left_child == None:
            self.left_child = newest
        else:
            temp = self.left_child
            self.left_child = newest
            newest.left_child = temp
        return newest
    def insert_right(self,newchild):
        newest = BinaryTree(newchild)
        if self.right_child == None:
            self.right_child = newest
        else:
            temp = self.right_child
            self.right_child = newest
            newest.right_child = temp
        return newest
    def getroot(self):
        return self.root
    def setroot(self,newroot):
        self.root = newroot
    def getleftchild(self):
        return self.left_child
    def getrightchild(self):
        return self.right_child
    def inorder_traversal(self):
        if self.left_child:
            self.left_child.inorder_traversal()
        print(self.root)
        if self.right_child:
            self.right_child.inorder_traversal()


class Stack:
    def __init__(self):
        self.data = []
        self.size =0
    def isEmpty(self):
        return self.size==0
    def push(self,element):
        self.size+=1
        self.data.append(element)
    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        else:
            return self.data.pop()

def buildparsetree(inp_expr):
    operators = ['+','-','*','/']
    inp_list = inp_expr.split()                     #Expression list is created.
    root_tree = BinaryTree(" ")                     #Root node so as to come out of expression tree
    S = Stack()
    S.push(root_tree)                               #Root node is pushed in the Stack
    current_tree = root_tree                        #Current tree is the current subtree

    for i in inp_list:
        if i =='(':                                 #Rule 1
            current_tree.insert_left(" ")
            S.push(current_tree)
            current_tree = current_tree.getleftchild()

        elif i in operators:                        #Rule 3
            current_tree.setroot(i)
            current_tree.insert_right(" ")
            S.push(current_tree)
            current_tree = current_tree.getrightchild()
        elif i ==')':                               #Rule 2
            current_tree = S.pop()
        else:                                       #Rule 4
            current_tree.setroot(int(i))
            current_tree = S.pop()
    return root_tree

#expr_tree = buildparsetree("( ( 4 + 3 ) * 7 )")
#expr_tree.inorder_traversal()