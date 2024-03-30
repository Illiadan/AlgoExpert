array = [8, 5, 2, 9, 5, 6, 3]


def bubbleSort(array):

    isSorted = False
    length = len(array) - 1
    while isSorted is not True:
        isSorted = True
        for idx in range(length):
            if array[idx] > array[idx + 1]:
                array[idx], array[idx + 1] = array[idx + 1], array[idx]
                isSorted = False
        length -= 1

    return array


result = bubbleSort(array)
print(result)
