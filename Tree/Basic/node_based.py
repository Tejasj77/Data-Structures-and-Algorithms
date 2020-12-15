class BinaryTree:
    level = 0
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
        if self.right_child == None:
            newest = BinaryTree(newchild)
            self.right_child = newest
        else:
            newest = BinaryTree(newchild)
            temp = self.right_child
            self.right_child = newest
            newest.right_child = temp
        return newest
    def getroot(self):
        return self.root
    def getleftchild(self):
        return self.left_child
    def getrightchild(self):
        return self.right_child
    def __str__(self):
        return str(self.root)
    def __iter__(self):
        return iter(self.root)

"""
t = BinaryTree('a')
b = t.insert_left('b')
c = t.insert_right('c')
print(t.getleftchild())
print(t.getrightchild())
b.insert_left('d')
b.insert_right('e')
c.insert_left('f')
print(b.getleftchild())
print(b.getrightchild())
print(c.getleftchild())
print(t.level)
print(c.level)

"""
R = BinaryTree('a')
R.insert_left('b')
c = R.insert_right('c')
print(R.getleftchild())
print(R.getrightchild())

c.insert_left('f')
print(c.getleftchild())
R.insert_left(1)
print(R.getleftchild())
R.insert_right(1)
print(R.getrightchild())
print(R.level)

