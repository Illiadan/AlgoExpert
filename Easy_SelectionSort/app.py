array = [8, 5, 2, 9, 5, 6, 3]


def selectionSort(array):

    idx = 0
    while idx < len(array):
        print(array)
        smallestNumber = array[idx]
        smallestIdx = idx
        jdx = idx + 1
        while jdx < len(array):
            print(f"{jdx} - {smallestNumber}")
            if array[jdx] < smallestNumber:
                print(f"Swap {smallestNumber} with {array[jdx]}")
                smallestNumber = array[jdx]
                smallestIdx = jdx
            jdx += 1
        array[idx], array[smallestIdx] = array[smallestIdx], array[idx]
        idx += 1

    return array


result = selectionSort(array)
print(result)
