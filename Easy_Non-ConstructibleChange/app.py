coins = [5, 7, 1, 1, 2, 3, 22]
c1 = [1, 1, 1, 1, 1]

def nonConstructibleChange(coins):
    
    coinsSorted = sorted(coins)
    currChangeMaximum = 0

    for coin in coinsSorted:
        if coin > currChangeMaximum + 1:
            return currChangeMaximum + 1
        else:
            currChangeMaximum += coin
    return currChangeMaximum + 1
    
result = nonConstructibleChange(c1)
print(result)
