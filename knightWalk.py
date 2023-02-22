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
    visited = set()
    # Moves are the possible legal moves for the knight
    moves =[(1,2),(1,-2),(2,1),(2,-1),(-1,-2),(-1,2),(-2,-1),(-2,1)]
# Convert the letter code to a number betweeen 0 & 7
    dest = (boardx.index(end[0]),end[1])
    start = (boardx.index(start[0]),start[1],0)
    queue.append(start)
    count = 0
    while (queue):

        # G
        # If there are items in the queueu get the first Item
        currentLoc = queue.pop(0)

        # check if at destination
        
        if currentLoc[0]==dest[0] and currentLoc[1]==dest[1]:
            return f" Destination {end} reached in {currentLoc[2]} jumps" 

        # add to visited, no need to store the jumps score
        check = (currentLoc[0],currentLoc[1])
        if check not in visited:
            visited.add(check)
   
        for i in range(8):
            # Calculate the possible list of next positions
            newLoc = (currentLoc[0]+moves[i][0],currentLoc[1]+moves[i][1],currentLoc[2]+1)
            # If the possible steps are "off the board" ie <0 >7 for x or y then discount
            if newLoc[0]>=0 and newLoc[0]<=7 and newLoc[1]>=0 and newLoc[1]<=7:            
                queue.append(newLoc)

    return "Not possible to get to destination"

start = ('d',4)
end = ('g',0)
print(knightWalk(start,end))