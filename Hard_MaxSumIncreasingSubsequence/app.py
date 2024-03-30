array = [10, 70, 20, 30, 50, 11, 30]
array2 = [-1, 1]
array3 = [10, 15, 4, 5, 11, 14, 31, 25, 31, 23, 25, 31, 50]


def maxSumIncreasingSubsequence(array):
    # Write your code here.
    solutions = []
    for idx in range(len(array)):
        solutions.append([idx])
        for s in solutions:
            if array[idx] > array[s[-1]]:
                s.append(idx)
    for idx in reversed(range(len(array))):
        for s in solutions:
            if idx < s[0] and array[idx] < array[s[0]] and sum(s) < sum(s) + array[idx]:
                solutions.insert(0, s.copy())
                s.insert(0, idx)
    transformIdxToNumber(array, solutions)
    sums = sumUpArrays(solutions)
    return max(sums, key=lambda x: x[0])


def transformIdxToNumber(sourceArray, transformArray):
    for idx in range(len(transformArray)):
        for idy in range(len(transformArray[idx])):
            transformArray[idx][idy] = sourceArray[transformArray[idx][idy]]
    return transformArray


def sumUpArrays(arrays):
    sums = []
    for array in arrays:
        sums.append([sum(array), array])
    return sums


print(maxSumIncreasingSubsequence(array3))

"""
Input:
[10,70,20,30,50,11,30]

Output:
[110, [10,20,30,50]]

Idea:
[8,12,2,3,15,5,7]
-> [35,[8,12,15]]

8:  [[8]]
12>8:   [[8,12]]
2<12:   [[8,12],[2]]
3<12&3>2:   [[8,12],[2,3]]
15>12&15>3: [[8,12,15],[2,3,15]]
5<15&5<15:  [[8,12,15],[2,3,15],[5]]
7<15&7<15&7>5:  [[8,12,15],[2,3,15],[5,7]]

7:  [[8,12,15],[2,3,15],[5,7]]
5:  [[8,12,15],[2,3,15],[5,7]]
15>5:   [[8,12,15],[2,3,15],[5,7]]
3<5:    [[8,12,15],[2,3,15],[3,5,7]]
2<3:    [[8,12,15],[2,3,15],[2,3,5,7]]
12>2&12>2:  [[8,12,15],[2,3,15],[2,3,5,7]]
8>2&8>2:    [[8,12,15],[2,3,15],[2,3,5,7]]

-> max(sum()) -> max(35,20,17) -> 35
-> [35,[8,12,15]]

-------
10:     [[10]]
70>10:  [[10,70]]
20<70:  [[10,70],[20]]
30<70&30>20:    [[10,70],[20,30]]
50<70&50>30:    [[10,70],[20,30,50]]
11<70&11<50:    [[10,70],[20,30,50],[11]]
30<70&30<50&30>11:  [[10,70],[20,30,50],[11,30]]

30: [[10,70],[20,30,50],[11,30]]
11: [[10,70],[20,30,50],[11,30]]
50>11:  [[10,70],[20,30,50],[11,30]]
30>11:  [[10,70],[20,30,50],[11,30]]
20>11:  [[10,70],[20,30,50],[11,30]]
70>20&70>11:    [[10,70],[20,30,50],[11,30]]
10<20&10<11:    [[10,70],[10,20,30,50],[10,11,30]]

-> max(sum()) -> max(80,110,51) -> 110
-> [110,[10,20,30,50]]
"""
