array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
array2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2]
array3 = [1, 2, 4, 7, 10, 11, 7, 12, 13, 14, 16, 18, 19]
array4 = [4, 8, 7, 12, 11, 9, -1, 3, 9, 16, -15, 11, 57]


def subarraySort(array):
    # Write your code here.
    start = -1
    end = -1
    corruption = False

    for idx in range(len(array) - 1):
        if array[idx + 1] < array[idx]:
            corruption = True
            if start == -1:
                start = idx + 1
            else:
                end = idx + 1
        else:
            if corruption:
                if array[idx + 1] > array[start - 1]:
                    end = idx
                    corruption = False
                else:
                    end = idx + 1
    if start != -1:
        if end == -1:
            end = len(array) - 1
        minimum = min(array[start : end + 1])
        for idy in range(start + 1):
            if minimum < array[idy]:
                start = idy
                break
        maximum = max(array[start : end + 1])
        for idy in range(end, len(array)):
            if array[idy] < maximum:
                end = idy

    return [start, end]


print(subarraySort(array))

"""
Input:
[1,2,4,7,10,11,7,12,6,7,16,18,19]

Output:
[3,9]

Idea:
start=-1
end=-1
false=0
2>=1:   True
4>=2:   True
7>=4:   True
10>=7:  True
11>=10: True
7>=11:  False -> false=1, if start == -1: start=idx+1
12>=7:  True -> if false == 1: end=idx+1, false=0
6>=12:  False -> false=1, if start == -1: --- else: end=idx+1
7>=6:   True -> if false == 1: end=idx+1, false=0
16>=7:  True
18>=16: True
19>=18: True
minimum=min(array[start], array[end]) -> 6
for idy in range(0,start+1)
    if minimum<array[idy]:
        start = idy
        break
return [start, end]

-------
[1, 2, 4, 7, 10, 11, 7, 12, 13, 14, 16, 18, 19]
7<11: start=6
12<7: end=6
"""
