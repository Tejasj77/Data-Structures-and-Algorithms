def move_disk(index,from_p,to_p):
    print("Move disk", index," move from" , from_p , "to", to_p)

#Move the disk from pole to pole
#The disks are numbered from top to bottom. 0 .... n-1
def move_tower(height,from_pole,to_pole,with_pole):
    if height>=1:
        move_tower(height-1,from_pole,with_pole,to_pole)
        move_disk(height-1,from_pole,to_pole)
        move_tower(height-1,with_pole,to_pole,from_pole)


move_tower(3,'A','C','B')