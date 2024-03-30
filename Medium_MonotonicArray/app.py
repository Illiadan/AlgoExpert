array = [-1, -5, -10, -1100, -900, -1101, -1102, -9001]


def isMonotonic(array):
    """Function checks if array is monotonic and returns respective boolean value.
    An array is monotonic, if its elements from left to right are entirely non-increasing 
    or non-decreasing."""
    if len(array) < 2:
        return True

    for idx in range(len(array) - 1):
        delta = array[idx + 1] - array[idx]
        if delta < 0:
            return isMonotonicHelper(array, idx, "dec")
        elif delta > 0:
            return isMonotonicHelper(array, idx, "inc")
        else:
            continue
    return True


def isMonotonicHelper(array, idx, delta):

    for jdx in range(idx, len(array) - 1):
        if delta == "dec" and array[jdx + 1] > array[jdx]:
            return False
        if delta == "inc" and array[jdx + 1] < array[jdx]:
            return False
    return True


result = isMonotonic(array)
print(result)
