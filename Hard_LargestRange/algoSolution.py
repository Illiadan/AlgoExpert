array = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]

# O(n) time | O(n) space
def largestRange(array):
    # Write your code here.
    range = []
    length = 0
    nums = {}

    for num in array:
        nums[num] = True

    for num in array:
        if not nums[num]:
            continue
        nums[num] = False
        currLength = 1
        left = num - 1
        right = num + 1
        while left in nums:
            nums[left] = False
            currLength += 1
            left -= 1
        while right in nums:
            nums[right] = False
            currLength += 1
            right += 1
        if currLength > length:
            length = currLength
            range = [left + 1, right - 1]
    return range


print(largestRange(array))

""""
Input:
[1,11,3,0,15,5,2,4,10,7,12,6]

Output:
[0,7]

Idea:
{
    0: True
    1: True
    2: True
    ...
}
-> 0: False -> 1: False -> ... -> 7: False -> length = 8, range = [0,7] 
"""
