def number_of_paths(m,n):
    #Going in reverse order from bottom right to top-left.
    if(m==0 or n==0):                           #The top-row or top-column is reached i.e.y 1 is returned.
        return 1                                #1 is path is returned becoz a path is found to top-left
    else:
        #Decrementing row number and column no. to reach top-left corner.
        return number_of_paths(m-1,n) + number_of_paths(m,n-1)
m = int(input())
n = int(input())
print(number_of_paths(m-1,n-1))
