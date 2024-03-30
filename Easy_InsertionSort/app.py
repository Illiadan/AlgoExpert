array = [8, 5, 2, 9, 5, 6, 3]


def insertionSort(array):

    for idx in range(len(array)):
        jdx = idx
        while jdx > 0:
            if array[jdx] < array[jdx - 1]:
                array[jdx], array[jdx - 1] = array[jdx - 1], array[jdx]
            jdx -= 1

    return array


result = insertionSort(array)
print(result)
