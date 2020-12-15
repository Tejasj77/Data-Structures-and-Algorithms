#Size of area = M X N
# If N is odd and M is even, then add N to the total number of tiles required, then recompute for N/2 X M/2.
# If M is odd and N is even, then add M to the total number of tiles required, then recompute for N/2 X M/2.
# If M is odd and N is odd, then add (N+M)-1 to the total number of tiles required, then recompute for N/2 X M/2
# If M is even and N is even, then just recompute for N/2 X M/2 because for even no. of tiles the halving
# doesn't change the number of tiles.

def minTiles(m,n):
     if n==0 or m==0:
         return 0
     elif m%2==0 and n%2==1:
         return (m + minTiles(int(m/2),int(n/2)))
     elif m%2==1 and n%2 ==0:
         return (n + minTiles(int(m/2),int(n/2)))
     else:
         return (n+ m - 1 + minTiles(int(m/2),int(n/2)))

print(minTiles(5,10))