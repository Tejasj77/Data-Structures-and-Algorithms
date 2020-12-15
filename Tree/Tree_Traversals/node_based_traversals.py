class BinaryTree:
    level=0
    def __init__(self,root):
        self.root = root
        self.left_child = None
        self.right_child = None
    def insert_left(self,newchild):
        if self.left_child == None:
            newest = BinaryTree(newchild)
            self.left_child = newest
        else:
            newest = BinaryTree(newchild)
            temp = self.left_child
            self.left_child = newest
            newest.left_child = temp
        self.level +=1
        return newest
    def insert_right(self,newchild):
        if self.right_child ==None:
            newest = BinaryTree(newchild)
            self.right_child = newest
        else:
            newest = BinaryTree(newchild)
            temp = self.right_child
            self.right_child = newest
            newest.right_child = temp
        self.level +=1
        return newest
    def getrootval(self):
        return self.root
    def getleftchild(self):
        return self.left_child
    def getrightchild(self):
        return self.right_child
    def __str__(self):
        return str(self.root)
    def inorder(self):
        if self.left_child:
            self.left_child.inorder()
        print(self.root)
        if self.right_child:
            self.right_child.inorder()
    def preorder(self):
        print(self.root)
        if self.left_child:
            self.left_child.preorder()
        if self.right_child:
            self.right_child.preorder()
    def postorder(self):
        if self.left_child:
            self.left_child.postorder()
        if self.right_child:
            self.right_child.postorder()
        print(self.root)

T = BinaryTree(1)
a = T.insert_left(2)
b = T.insert_right(3)
a.insert_left(4)
a.insert_right(5)

print("The inorder traversal is")
T.inorder()
print('The preorder traversal is')
T.preorder()
print("The postorder traversal is")
T.postorder()


