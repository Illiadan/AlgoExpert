array = [2, 5, -3, -4, 6, 7, 2]
array2 = [1, 2, 3, 4, 1, 2, 3, 4, -8, -7, 6, 2, 17, 2, -8, 9, 0, 2]


def nextGreaterElement(array):
    # Write your code here.
    if len(array) == 0:
        return []
    out = [0 for x in array]
    maxValue = max(array)
    maxIdx = array.index(maxValue)
    for idx in range(maxIdx, maxIdx - len(array), -1):
        if array[idx] == maxValue:
            out[idx] = -1
        elif array[idx] < array[idx + 1]:
            out[idx] = array[idx + 1]
        else:
            y = 1
            while array[idx] >= out[idx + y]:
                y += 1
            out[idx] = out[idx + y]
    return out


print(nextGreaterElement(array))
print(nextGreaterElement(array2))

"""
Input:
[2, 5, -3, -4, 6, 7, 2]

Output:
[5, 6, 6, 6, 7, -1, 5]

Idea:
range(len(array)-1,-2,-1)
max(array)
idx 6 == max(array)? -> idx 6 == len(array) - 1? -> max(array)
idx 5 == max(array)? -> -1
idx 4 == max(array)? -> idx 4 == len(array) - 1? -> idx 4 < idx 5? -> array[idx 5]
idx 3 == max(array)? -> idx 3 == len(array) - 1? -> idx 3 < idx 4? -> array[idx 4]
idx 2 == max(array)? -> idx 2 == len(array) - 1? -> idx 2 < idx 3? -> idx 2 < out[idx 3]? -> out[idx 3]
idx 1 == max(array)? -> idx 1 == len(array) - 1? -> idx 1 < idx 2? -> idx 1 < out[idx 2]? -> out[idx 2]
idx 0 == max(array)? -> idx 0 == len(array) - 1? -> idx 0 < idx 1? -> array[idx 1]
idx -1 == max(array)? -> idx -1 == len(array) - 1? -> idx -1 < idx 0? -> idx -1 < out[idx 0]? -> out[idx 0]
"""
