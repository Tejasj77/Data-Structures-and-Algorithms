m = 4
n = 4
matrix = [[0]*n for i in range(m)]
#print(matrix)
value_list = [1,2,3,4,1,2,3,4,1,2,3,4,1,3,2,4]
iter=0

for i in range(m):
    for j in range(n):
        matrix[i][j] = value_list[iter]
        iter+=1

#starting_point = tuple(map(int,input().split()))
#color = int(input())
#previous_color = matrix[starting_point[0]][starting_point[1]]

def legalmove(coor,matsize,block,prev_color):
    if(0<=coor[0]<matsize[0] and 0<=coor[1]<matsize[1] and block[coor[0]][coor[1]]==prev_color):
        return True
    return False

def possible_moves(a,b,size,block,prev):
    legmoves = []
    move_offsets = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for i in move_offsets:
        newX = a + i[0]
        newY = b + i[1]

        if legalmove((newX,newY),size,block,prev):
            legmoves.append((newX,newY))
    return legmoves


def send(points,size,limit,block,prev,color,path):
    if (limit==(size[0]*size[1])) or (block[points[0]][points[1]]!=prev) or (block[points[0]][points[1]] in path):
        #print("The Road has ended")
        limit+=1
        #print((points[0],points[1]))
        return
    else:
        print("Here and there")
        block[points[0]][points[1]] = color
        path.append(points)
        limit+=1
        movable_coordinates = possible_moves(points[0],points[1],size,block,prev)
        for i in movable_coordinates:
            send(i,size,limit,block,prev,color,path)
    return


#send(starting_point,(m,n),0,matrix,previous_color,color,[])
#print(matrix)

matrix1 = [[1,1,1],[1,1,0],[1,0,1]]
print(matrix1)
send((1,1),(3,3),0,matrix1,matrix1[1][1],2,[])
print(matrix1)
