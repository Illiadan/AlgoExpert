n = 7
denoms = [1, 5, 10]


# O(nd) time | O(n) space
def minNumberOfCoinsForChange(n, denoms):
    """Function takes in an array of positive integers representing coin
    denominations and a single non-negative integer n representing a target
    amount of money and returns the smallest number of coins to make change for 
    that target amount using the given coin denominations."""
    numOfCoins = [float("inf") for amount in range(n + 1)]
    numOfCoins[0] = 0
    for denom in denoms:
        for amount in range(len(numOfCoins)):
            if denom <= amount:
                numOfCoins[amount] = min(numOfCoins[amount],
                                         numOfCoins[amount - denom] + 1)
    return numOfCoins[n] if numOfCoins[n] != float("inf") else -1


result = minNumberOfCoinsForChange(n, denoms)
print(result)
