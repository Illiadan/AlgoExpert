array = [5, 1, 4, 2]


def arrayOfProducts(array):
    """Function that returns an array of same length as input array,
    where each element of output array is equal to the product of
    every other element in the input array."""
    temp = 1
    out = []
    for idx in range(len(array)):
        for jdx in range(len(array)):
            if idx == jdx:
                continue
            temp *= array[jdx]
        out.append(temp)
        temp = 1
    return out


result = arrayOfProducts(array)
print(result)
