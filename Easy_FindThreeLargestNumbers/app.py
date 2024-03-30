array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]


def findThreeLargestNumbers(array):

    out = []
    for i in range(len(array)):
        if len(out) < 3:
            out.append(array[i])
            sorting(out)
        elif array[i] > out[0]:
            out.remove(out[0])
            out.append(array[i])
            sorting(out)

    return out


def sorting(array):

    if len(array) < 2:
        return array

    if len(array) == 2:
        if array[0] > array[1]:
            array[0], array[1] = array[1], array[0]
    else:
        if array[0] > array[1]:
            array[0], array[1] = array[1], array[0]
        if array[1] > array[2]:
            array[1], array[2] = array[2], array[1]
        if array[0] > array[1]:
            array[0], array[1] = array[1], array[0]

    return array


result = findThreeLargestNumbers(array)
print(result)
