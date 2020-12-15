from pythonds.graphs import Graph,Vertex
import inspect
p = inspect.getsource(Graph)

def genlegalmov(x,y,size):
    newmoves = []       #List of tuples for storing all the possible moves
    movoffsets= [(-1,-2),(-1,2),(-2,-1),(-2,1),     #Offset to any position for the knight to travel. Adich ghar.
                 (1,-2),(1,2),(2,-1),(2,1)]
    #Iterating through all the offsets
    for loc in movoffsets:
        newX = x + loc[0]   #Adding the x co-ordinate of the offset to the current position
        newY = y + loc[1]   #Adding the y co-ordinate of the offset to the current position

        if poslegal(newX,size) and poslegal(newY,size):  #Checking if the position exists on the chess board
            newmoves.append((newX,newY))                 #Appending the move to the list of newmoves
    return newmoves

def poslegal(x,s):
    #Checking if the position exists on the chess board
    if x>=0 and x<s:
        return True
    return False

def convloctoNode(row,col,size):
    #Simple algo to convert row and col position into a Node
    return (row,col)

def knightpathgraph(bdsize):
    ktgraph = Graph()   #Empty Graph
    for row in range(bdsize+1):     #Iterating through rows and columns
        for col in range(bdsize+1):
            nodeID = convloctoNode(row,col,bdsize) #Converting the rows and cols position to a Node
            legalmov = genlegalmov(row,col,bdsize) #Calculating all the available moves of a knight

            for e in legalmov:                      #Iterating through all the available moves
                newid = convloctoNode(e[0],e[1],bdsize) #Converting the available move into a Node
                ktgraph.addEdge(nodeID,newid)           #Adding edge betwwen the current Node and the available Node
    return ktgraph                                  #Thus, a graph of moves is built

k1 = knightpathgraph(6)

def dfs(n,path,u,limit):
    u.setColor('gray') #The Node has been visited and set the color to gray
    path.append(u)      #Append the node to the path
    if n<limit:         #Number of times the node has been visited
        nbrList = list(u.getConnections())  #Visit the adjacent node
        i=0
        done=False
        while i<len(nbrList) and not done:  #while all adjacent nodes traversed and the end vertex is not reached
            if nbrList[i].getColor() == 'white':        #The node is not traversed
                done,path = dfs(n+1,path,nbrList[i], limit)  #Repeat above steps for the new node #Recursion
            i=i+1
        if not done:            #Reached a dead end. No further adjacent node
            path.pop()          #Backtrack
            u.setColor('white')
    else:
        done = True             #End node is reached
    return done,path

fin1,fin2 = dfs(0,[],k1.getVertex((0,0)),63)

print(len(fin2))
for i in fin2:
    print(i.id)
#The nodes traversed list
# for i in fin2:
#     print(i)


