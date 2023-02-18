#A breadth first graph search returning a list of nodes from a dictionary that defines the connectons in a graph
# eg node 0 connects to 2, 5, 6
# graph={O:[2,5,6]}
'''
GRAPH
					10				 6
						\					\
			3			2					1	
			 \		\				 / \
			 0----5-------4	 7
			/							\
		 9							8


'''


graph = {
	0:[3,5,9], # 0 is connected t0 2 and 5 and 9
	1:[6,7,4],
	2:[10,5],
	3:[0],
	4:[1,5,8],
	5:[0,2,4],
	6:[1],
	7:[1],
	8:[4],
	9:[0],
	10:[2]
}

def breadth_first(graph, start):
	result = [] # the returned list of visited nodes in order
	queue =[start]
	# if there are still nodes 
	while queue: 
		# get the first in the queue
		currentNode = queue.pop(0) 
		#add to visited
		result.append(currentNode)
		for connection in graph[currentNode]:
			if connection not in result:
				queue.append(connection)
	return result


if __name__ == '__main__':
	
	print(breadth_first(graph,0))
	 		
	

