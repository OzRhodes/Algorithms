# A binary search function
# It operates on a sort list
# It splits the list in half and assesses if the target is identified or in the upper or lower half of the list
# It then splits the selected half again and repeats until the list is exhausted or the target found



def binarySearch(nums, target):
 
    # search space is nums[left…right]
    left, right = 0, len(nums) - 1
 
    # loop till the search space is exhausted
    while left <= right:
 
        # find the mid-value in the search space and
        # compares it with the target
 
        mid = (left + right) // 2
 
        # overflow can happen. Use:
        # mid = left + (right - left) / 2
        # mid = right - (right - left) // 2
 
        # target is found
        if target == nums[mid]:
            return mid
 
        # discard all elements in the right search space,
        # including the middle element
        elif target < nums[mid]:
            right = mid - 1
 
        # discard all elements in the left search space,
        # including the middle element
        else:
            left = mid + 1
 
    # `target` doesn't exist in the list
    return None
 
 
if __name__ == '__main__':
 
    nums = [2, 5, 6, 8, 9, 10]
    target = 8
 
    index = binarySearch(nums, target)
 
    if index:
        print('Element found at index', index)
    else:
        print('Element found not in the list')
 
