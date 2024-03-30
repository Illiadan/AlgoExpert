array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
target = 33


def binarySearch(array, target):

    if target in array:
        return array.index(target)

    return -1


result = binarySearch(array, target)
print(result)
