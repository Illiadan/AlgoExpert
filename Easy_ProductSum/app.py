array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]


def productSum(array):

    return listSum(array, depth=1, pSum=0)


def listSum(array, depth, pSum):

    for a in array:
        if type(a) is int:
            calcDepth = depth
            multiplier = 1
            while calcDepth > 1:
                multiplier *= calcDepth
                calcDepth -= 1
            print(f"{pSum + a * multiplier} = {pSum} + {a} * {multiplier}")
            pSum += a * multiplier
        else:
            runningDepth = depth + 1
            pSum = listSum(a, runningDepth, pSum)

    return pSum


result = productSum(array)
print(result)
