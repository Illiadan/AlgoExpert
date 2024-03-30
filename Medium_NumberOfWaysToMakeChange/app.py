n = 7
denoms = [2, 3, 4, 7]


# O(nd) time | O(d) space
def numberOfWaysToMakeChange(n, denoms):
    """Function takes in an array of positive integers representing coin
    denominations and a single non-negative integer n representing a target
    amount of money and returns the number of ways to make change for that
    target amount using the given coin denominations."""
    ways = [0 for _ in range(n + 1)]
    ways[0] = 1
    for e in denoms:
        for idx in range(len(ways)):
            if e <= idx:
                ways[idx] += ways[idx - e]
    return ways[-1]


result = numberOfWaysToMakeChange(n, denoms)
print(result)
"""
6 | [1,5] => 6x1, 1x1+1x5
6 | [1,2,5] => 6x1, 1x1+1x5, 3x2, 4x1+2, 2x1+2x2
7 | [2,3,4,7] => 1x7, 1x4+1x3, 2x2+1x3
"""
