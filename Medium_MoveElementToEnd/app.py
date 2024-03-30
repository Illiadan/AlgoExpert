array = [2, 1, 2, 2, 2, 3, 4, 2]
toMove = 2


def moveElementToEnd(array, toMove):
    """Function shall move all instances of the toMove integer to the end of the array in place and returns the array"""

    for idx in range(len(array)):
        if array[idx] == toMove:
            jdx = idx + 1
            if jdx >= len(array):
                return array
            while jdx < len(array):
                if array[jdx] != toMove:
                    array[idx], array[jdx] = array[jdx], array[idx]
                    break
                else:
                    jdx += 1
                if jdx >= len(array):
                    return array
    return array


result = moveElementToEnd(array, toMove)
print(result)
