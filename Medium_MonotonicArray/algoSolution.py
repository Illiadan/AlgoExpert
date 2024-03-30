array = [-1, -5, -10, -1100, -900, -1101, -1102, -9001]


def isMonotonic(array):
    """Function checks if array is monotonic and returns respective boolean value.
    An array is monotonic, if its elements from left to right are entirely non-increasing 
    or non-decreasing."""
    isNonDecreasing = True
    isNonIncreasing = True
    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            isNonDecreasing = False
        if array[i] > array[i - 1]:
            isNonIncreasing = False
    return isNonDecreasing or isNonIncreasing


result = isMonotonic(array)
print(result)
