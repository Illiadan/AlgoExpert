array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]


def longestPeak(array):
    """Function returns length of longest peak in the array.
    A peak is defined as adjacent integers that are strictly increasing until
    they reach a tip, at which point they become strictly decreasing.
    At least threee integers are required to form a peak."""
    lenArray = len(array)
    idxList = []
    counter = 0

    if lenArray < 3:
        return 0

    for idx in range(1, lenArray - 1):
        if array[idx - 1] < array[idx] and array[idx] > array[idx + 1]:
            idxList.append(idx)

    if idxList == []:
        return 0

    for idx in idxList:
        out = checkNeighbours(array, idx, lenArray)
        if counter < out:
            counter = out
    return counter


def checkNeighbours(array, idx, lenArray):
    l = 2
    r = 2
    counter = 3
    while idx - l >= 0 and array[idx - l] < array[idx - l + 1]:
        counter += 1
        l += 1
    while idx + r < lenArray and array[idx + r] < array[idx + r - 1]:
        counter += 1
        r += 1
    return counter


result = longestPeak(array)
print(result)
