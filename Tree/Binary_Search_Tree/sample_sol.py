import pandas as pd

book = pd.read_excel('Sample_Book.xlsx')
sr_no = list(book["Sr No."])
content = list(book["Content"])
page_no = list(book["Page"])
global final
# a = 1
# b = 1.1
# c = "1.1.1"
# d = "2.1.1.1"
# print(float(b),int(b))
# if '.' in c:
#     print(True)
#
# count = sum(map(lambda x:1 if '.' in x else 0,d))
# print(count,d[0])

class Node:
    def __init__(self,key,value,page):
        self.key = key
        self.value = value
        self.page = page
        self.child = []
        self.parent = None
    def has_parent(self):
        return self.parent!=None
    def has_child(self):
        return self.child!=None
    def is_leaf(self):
        return self.child==None
    def is_root(self):
        return self.parent==None
    def add_parent(self,parent):
        self.parent = parent
    def add_children(self,child_node):
        self.child.append(child_node)

    def __str__(self):
        return str(self.key)

class BinaryTree:
    def __init__(self,name):
        self.root = Node("Book_name",name,0)
        self.size = 0
        self.last_page = 0
    def getrootnode(self):
        return self.root

    def update_last_page(self,lastpage):
        if lastpage>self.last_page:
            self.last_page = lastpage
    def continuity_check(self,input_node,parent_node):
        return str(parent_node.key) in str(input_node.key) and str(parent_node.key)[0]==str(input_node.key)[0]

    def _putter(self,input_node,parent_node):
        for i in range(len(parent_node.child)):
            if self.continuity_check(input_node,parent_node.child[i]):
                self._put(input_node,parent_node.child[i])

    def _put(self,inp_node,parent):
        inp_counter = sum(map(lambda x:1 if '.' in x else 0,str(inp_node.key)))
        parent_counter = sum(map(lambda x:1 if '.' in x else 0,str(parent.key)))
        if inp_counter==parent_counter+1:
            if self.continuity_check(inp_node,parent):
                #print(parent," To ", inp_node)
                parent.add_children(inp_node)
                inp_node.add_parent(parent)
                self.update_last_page(inp_node.page)
                return True
        else:
            self._putter(inp_node,parent)

    def put(self,serial,text,pages):
        newnode = Node(serial,text,pages)
        if type(newnode.key)==int and (newnode.key%int(newnode.key)==0):
            #print(self.root, " To ", newnode)
            self.root.add_children(newnode)
            self.update_last_page(newnode.page)
        else:
            for iter in range(len(self.root.child)):
                if self.continuity_check(newnode,self.root.child[iter]):
                    self._put(newnode,self.root.child[iter])


    def get_chapter_through_string_bfs(self,word):
        queue = []
        queue.append(self.root)
        done = False
        while queue and not done:
            current = queue.pop()
            for iter in current.child:
                print("Visiting " , iter)
                if word in iter.value:
                    print("FOund Found Found")
                    print(iter)
                    done = True
                    break
                else:
                    queue.append(iter)
        if not done:
            print("The word was never used in this book")
            print("Get your facts straight")

    def get_chapter_through_string_dfs(self,start,word):
        for iter in start.child:
            #print("Visiting ", iter)
            if word not in iter.value:
                temp = self.get_chapter_through_string_dfs(iter,word)
                #print(temp)
                if temp:
                    return (temp)
            else:
                #print("Volllllaaaaa")
                #print(iter)
                #print(iter.key)
                return (iter)


    def get_chapter_through_page(self,number):
        if number > self.last_page:
            print("The Book is not written till this page")
        else:
            for iter in range(len(self.root.child)):
                if number<self.root.child[iter].page:
                    found = self.root.child[iter-1]
                    print(found,found.value,found.page)

    def traverse(self):
        for i in self.root.child:
            print("Chapter", i)
            for j in i.child:
                print(j)


root = BinaryTree("Content")
for iter in range(len(sr_no)):
    root.put(sr_no[iter],content[iter],page_no[iter])

#wanted_page = int(input())
#root.get_chapter_through_page(wanted_page)
wanted_string = input()
root.get_chapter_through_string_bfs(wanted_string)
#print(root.get_chapter_through_string_dfs(root.getrootnode(),wanted_string))