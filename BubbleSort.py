
# todo description

def bubble_sort(lst):
    '''Implementation of bubble sort algorithm'''

    for border in range(len(lst)-1, 0, -1):  
        for i in range(border):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return lst

list_to_sort = [27, 0, 71, 70, 27, 63, 90]
print(bubble_sort(list_to_sort))
