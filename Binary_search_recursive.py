# Recursive version of the  binary search algorithm
# It operates on a sort list
# It splits the list in half and assesses if the target is identified or in the upper or lower half of the list
# It then splits the selected half again and repeats until the list is exhausted or the target found

def binarySearch(nums, left, right, target):
 
    # Base condition (search space is exhausted)
    if left > right:
        return None
 
    # find the mid-value in the search space and
    # compares it with the target
 
    mid = (left + right) // 2
 
    # overflow can happen. Use below
    # mid = left + (right - left) / 2
 
    # Base condition (a target is found)
    if target == nums[mid]:
        return mid
 
    # discard all elements in the right search space,
    # including the middle element
    elif target < nums[mid]:
        return binarySearch(nums, left, mid - 1, target)
 
    # discard all elements in the left search space,
    # including the middle element
    else:
        return binarySearch(nums, mid + 1, right, target)
 
 
if __name__ == '__main__':
 
    nums = [2, 5, 6, 8, 9, 10]
    target = 9
 
    left, right = 0, len(nums) - 1
    
    index = binarySearch(nums, left, right, target)
 
    if index:
        print('Element found at index', index)
    else:
        print('Element found not in the list')
 
