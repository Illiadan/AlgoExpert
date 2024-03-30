array = [5, 1, 4, 2]


def arrayOfProducts(array):
    """Function that returns an array of same length as input array,
    where each element of output array is equal to the product of
    every other element in the input array."""
    products = [1 for _ in range(len(array))]

    leftRunningProduct = 1
    for i in range(len(array)):
        products[i] = leftRunningProduct
        leftRunningProduct *= array[i]

    rightRunningProduct = 1
    for i in reversed(range(len(array))):
        products[i] *= rightRunningProduct
        rightRunningProduct *= array[i]

    return products


result = arrayOfProducts(array)
print(result)
