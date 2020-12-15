class Node:
    def __init__(self,key,value,parent=None,left=None,right=None):
        self.key = key
        self.value = value
        self.parent = parent
        self.left_child = left
        self.right_child = right
        self.balanceFactor = 0
    def is_right_child(self):
        return self.parent and self.parent.right_child is self
    def is_left_child(self):
        return self.parent and self.parent.left_child is self

    def is_root(self):
        return not self.parent
    def has_left_child(self):
        return bool(self.left_child)
    def has_right_child(self):
        return bool(self.right_child)

class AVLTree:
    def __init__(self,root):
        self.root = root
        self.size = 0

    def rotate_left(self,rotation_root):
        new_root = rotation_root.right_child
        rotation_root.right_child = new_root.left_child
        if new_root.left_child:
            new_root.left_child.parent = new_root.left_child
        new_root.parent = rotation_root.parent
        if rotation_root.is_root():
            self.root = new_root
        else:
            if rotation_root.is_left_child():
                rotation_root.parent.left_child = new_root
            else:
                rotation_root.parent.right_child = new_root
        new_root.left_child = rotation_root
        rotation_root.parent = new_root
        rotation_root.balanceFactor = (
            rotation_root.balanceFactor + 1 - min(new_root.balanceFactor,0)
        )
        new_root.balanceFactor = (
            new_root.balanceFactor +1 + max(rotation_root.balanceFactor,0)
        )
    def rotate_right(self,rotation_root):
        new_root = rotation_root.left_child
        rotation_root.left_child = new_root.right_child
        if new_root.right_child:
            new_root.right_child.parent = rotation_root
        new_root.parent = rotation_root.parent
        if rotation_root.is_root():
            self.root = new_root
        else:
            if rotation_root.is_left_child():
                rotation_root.parent.left_child = new_root
            else:
                rotation_root.parent.right_child = new_root
        new_root.right_child = rotation_root
        rotation_root.parent = new_root
        rotation_root.balanceFactor = (
            rotation_root.balanceFactor+1-min(new_root.balanceFactor,0)
        )
        new_root.balanceFactor = (
            new_root.balanceFactor+1+max(rotation_root.balanceFactor,0)
        )

    def rebalance(self,node):
        if node.balanceFactor<0:
            if node.right_child.balanceFactor>0:
                self.rotate_right(node.right_child)
                self.rotate_left(node)
            else:
                self.rotate_left(node)
        else:
            if node.left_child.balanceFactor<0:
                self.rotate_left(node.right_child)
                self.rotate_right(node)
            else:
                self.rotate_right(node)

    def update_balance(self,node):
        if node.balanceFactor >1 or node.balanceFactor<-1:
            self.rebalance(node)
            return
        if node.parent:
            if node.is_left_child():
                node.parent.balanceFactor +=1
            elif node.is_right_child():
                node.parent.balanceFactor -=1
            if node.parent.balanceFactor !=0:
                self.update_balance(node.parent)

    def _put(self,key,value,current_node):
        if key<current_node.key:
            if current_node.has_left_child():
                self._put(key,value,current_node.left_child)
            else:
                current_node.left_child = Node(key,value,parent=current_node)
                self.update_balance(current_node.left_child)
        else:
            if current_node.has_right_child():
                self._put(key,value,current_node.right_child)
            else:
                current_node.right_child = Node(key,value,parent=current_node)
                self.update_balance(current_node.right_child)

    def put(self,key,value):
        if self.root:
            self._put(key,value,self.root)
        else:
            self.root = Node(key,value)
        self.size +=1

