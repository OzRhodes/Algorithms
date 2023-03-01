def quick_sort(data):
    """
    @type data: list
    A recursive apporach to quicksorting a lit
    """
    if len(data) <= 1:
        return data

    pivot = len(data)-1  # choose the last component as pivot
    i = -1
    for j in range(0, len(data)-1):
        if data[j] < data[pivot]:
            i += 1
            data[i], data[j] = data[j], data[i]  # swap
            
    data[pivot], data[i+1] = data[i+1], data[pivot]
    
    return quick_sort(data[:i+1]) + [data[i+1]] + quick_sort(data[i+2:])



data = [1,6,4,5,8,2,9,7]
print(quick_sort(data))
