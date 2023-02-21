'''
A knight o a chess board must move from its original location
to a new location.
How many steps does it take?
'''

'''
 The chess board is 8x8
 A-H
 0-7

 the knight has to stay on the board 
 and move in a 2 x 1L shape

 1 up/down 2 across or 2 up/down 1 across 

  A B C D E F G H
 0
 1
 2
 3
 4
 5
 6
 7
  '''


def knightWalk(start, end):
    boardx = ['a','b','c','d','e','f','g','h']
    queue = []
    visited =[]
    moves =[(1,2),(1,-2),(2,1),(2,-1),(-1,-2),(-1,2),(-2,-1),(-2,1)]
    jumps = 1

    dest = (boardx.index(end[0]),end[1])
    start = (boardx.index(start[0]),start[1],0)
    visited.append(start)
    queue.append(start)

    while (queue):
        currentLoc = queue.pop()
        for i in range(8):
            # Calculate the possible list of next positions
            newLoc = (currentLoc[0]+moves[i][0],currentLoc[1]+moves[i][1],jumps)
            # check to see if you are at the destination
            if newLoc[0]==dest[0] and newLoc[1] ==dest[1]:
                return (f"Destination {dest} reached and it took {jumps} jumps")
            # If the possible steps are "off the board" ie <0 >7 for x or y then discount
            if newLoc[0]>=0 and newLoc[0]<=7 and newLoc[1]>=0 and newLoc[1]<=7:
                if newLoc not in visited:
                    queue.append(newLoc)
                    visited.append(newLoc)
                    print(visited)
            jumps +=1

    return "Not possible to get to destination"




    
    return


# Add the list of possile locations to a queue with the 'cost/step number'
# step through the queue to see if the position is the destination and if not,
# Add these positions to the queue

start = ('d',4)
end = ('h',3)
print(knightWalk(start,end))