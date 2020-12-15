#Drawing1
#The list of list representation of Drawing1 Tree is :

tree = [
    'a',
    ['b',['d',[],[]],['e',[],[]]],['c',['f',[],[]]]
]

"""
print("Root element is ", tree[0])
print("Left subtree is ", tree[1])
print("Right subtree is ", tree[2])
print("Left subtree of Left  subtree is ", tree[1][1])
print("Right subtree of Left subtree is ", tree[1][2])
print("Right subtree of Right subtree is ", tree[2][1])
"""
#Now converting to Drawing2
#A function to create a tree and insert inside the tree

def BinaryTree(root):
    return [root,[],[]]
def insert_left(root,newchild):
    current = root.pop(1)
    if len(current)>1:
        root.insert(1,[newchild,current,[]])
    else:
        root.insert(1,[newchild,[],[]])
    return root[1]
def insert_right(root,newchild):
    current = root.pop(2)
    if len(current)>1:
        root.insert(2,[newchild,[],current])
    else:
        root.insert(2,[newchild,[],[]])
    return root[2]
def getrootval(root):
    return root[0]
def getleftchild(root):
    return root[1]
def getrightchild(root):
    return root[2]

#Creation of Drawing1
drawing1 = BinaryTree('a')
first_level_left = insert_left(drawing1,'b')
first_level_right = insert_right(drawing1,'c')

#print(getleftchild(drawing1))
#print(getleftchild(first_level_left))
insert_left(first_level_right,'f')
insert_left(first_level_left,'d')
insert_right(first_level_left,'e')
for i in drawing1:
    print(i)
#Converting to Drawing2
insert_left(drawing1,'z')           #Adding z in between the original tree.
insert_left(first_level_right,'x')  #Adding x after c.

for i in drawing1:
    print(i)
