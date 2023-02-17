'''
sorting a list of numbers
start with a sorted list of 1 then insert by comparing neighbors
eg

unsorted list
5 6 8 4 3 2

take first and mark as sorted

Sorted              Unsorted
5         |       6 8 4 3 2
next 6 is greated than 5 so acc
5 6       |				8 4 3 2
next 8 is greater than 8 so append
5 6 8     | 			4 3 2
next 4 is less than 8 so swap 4 and 8
5 6 4 8		|				3 2
4 is less than 6 so swap 4 and 6
5 4 6 8 	|				3 2
4 is less than 5 so swap 4 and 5
4 5 6 8 	|				3 2
continue until all sorted

'''


def insert_sort(list):
# step through the list
	for counter1 in range(1,len(list)):
		counter2 = counter1
# swap if needed - Simultaneous reassignment 
		while list[counter2-1] > list[counter2] and counter2 >0:
			list[counter2-1], list[counter2] = list[counter2], list[counter2-1]
			counter2 -=1
	return list
			
	
	
list = [5,6,8,4,3,2]
print(insert_sort(list))
