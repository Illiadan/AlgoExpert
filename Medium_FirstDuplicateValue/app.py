array = [2, 1, 5, 2, 3, 3, 4]


def firstDuplicateValue(array):
    """Function takes a non-empty array of positive integers and returns
    the first integer that appears more than once in the array, when read
    from left to right."""
    arraySet = set(array)

    for i in arraySet:
        if i in array:
            array.remove(i)
    if array == []:
        return -1
    else:
        return array[0]


result = firstDuplicateValue(array)
print(result)
