'''
imagine an m x n grid
how many ways can you traverse that grid 
starting at the top left if you can only move 
down and right 
A grid with m or m which is 1 or less a returns a 0 

Again this is a brute force solution as some calcuations are repeated
'''

def gridTraveller(m,n):
    if m==1 and n==1:
        return 1
    elif m==0 or n==0:
        return 0 
    else:
        return  gridTraveller(m-1,n) + gridTraveller(m,n-1)


print(gridTraveller(10,10))
