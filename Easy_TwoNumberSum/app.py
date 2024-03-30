array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10

def twoNumberSum(array, targetSum):

    #   time complexity O(n^2)
    """
    out = []
    isFound = False
    for int1 in array:
        i = targetSum - int1
        for int2 in array:
            if int2 == i and array.index(int1) != array.index(int2):
                out.append(int1)
                out.append(int2)
                isFound = True
                break
        if isFound:
            break
    return out
    """

    #   time complexity O(2n) = O(n)
    out = []
    resArray = []

    for a in array:
        resArray.append(targetSum - a)
    
    for b in resArray:
        if b in array and array.index(b) != resArray.index(b):
            out.append(b)
            out.append(array[resArray.index(b)])
            break
            
    return out

res = twoNumberSum(array, targetSum)
print(res)
