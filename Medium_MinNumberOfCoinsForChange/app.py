n = 7
denoms = [1, 5, 10]


# O(nd) time | O(n) space
def minNumberOfCoinsForChange(n, denoms):
    """Function takes in an array of positive integers representing coin
    denominations and a single non-negative integer n representing a target
    amount of money and returns the smallest number of coins to make change for 
    that target amount using the given coin denominations."""
    nums = [-1 for _ in range(n + 1)]
    nums[0] = 0
    for e in sorted(denoms):
        for idx in range(len(nums)):
            if e <= idx:
                if idx % e == 0:
                    if nums[idx] != -1:
                        nums[idx] = min(nums[idx], idx // e)
                    else:
                        nums[idx] = idx // e
                else:
                    if nums[idx - e] != -1:
                        nums[idx] = min(nums[idx], nums[idx - e] + 1)
    return nums[-1]


result = minNumberOfCoinsForChange(n, denoms)
print(result)
"""
4 | [2,3]
[0,-1,-1,-1,-1]
[0,-1,1,-1,2]
[0,-1,1,1,2]

10 | [1,5,10]
[0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
[0,1,2,3,4,5,6,7,8,9,10]
[0,1,2,3,4,1,2,3,4,5,2]
[0,1,2,3,4,1,2,3,4,5,1]

10 | [1,3,4]
[0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
[0,1,2,3,4,5,6,7,8,9,10]
[0,1,2,1,2,3,2,3,4,3,4]
[0,1,2,1,1,2,2,2,2,3,3]
"""
