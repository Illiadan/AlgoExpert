array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73, 355]
target = 70


def binarySearch(array, target):

    return binarySearchHelper(array, target, index=0)


def binarySearchHelper(array, target, index):

    print(array)
    print(index)

    if len(array) == 0:
        return -1

    newArray = []
    if target == array[len(array) // 2]:
        index += len(array) // 2
        return index
    elif target < array[len(array) // 2]:
        newArray = array[:len(array) // 2]
        index = binarySearchHelper(newArray, target, index)
    else:
        newArray = array[len(array) // 2 + 1:]
        out = binarySearchHelper(newArray, target, index=len(array) // 2 + 1)
        if out == -1:
            return -1
        index += out

    return index


result = binarySearch(array, target)
print(result)
