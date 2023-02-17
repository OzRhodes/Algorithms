#A breadth first search of a binary tree
#Returns a list for the nodes from a breadth first search 
from collections import deque

class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n
        
        
def tree_by_levels(node):
    result = []
    if node != None:
    	
	    queue = deque()
	    queue.append(node)
	    #while node != None:
	    while len(queue)>0:
		    q_node = queue.popleft()
		    if q_node.left != None:
		    	queue.append(q_node.left)
		    if q_node.right != None:
		    	queue.append(q_node.right)
		    result.append(q_node.value)

    return result


#print(tree_by_levels((None,None,4)))
#print(tree_by_levels(Node(Node(None, Node(None, None, 4), 2), Node(Node(None, None, 5), Node(None, None, 6), 3), 1)))

