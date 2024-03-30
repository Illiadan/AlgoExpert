array = [7, 6, 4, -1, 1, 2]
targetSum = 16


def fourNumberSum(array, targetSum):
    # Write your code here.
    out = []
    foundSums = {}

    for idx in range(1, len(array) - 1):
        for idy in range(idx + 1, len(array)):
            diff = targetSum - (array[idx] + array[idy])
            if diff in foundSums:
                values = foundSums[diff]
                for value in values:
                    out.append([value[0], value[1], array[idx], array[idy]])

        for idz in range(0, idx):
            sum = array[idx] + array[idz]
            if sum in foundSums:
                values = foundSums[sum]
                values.append([array[idx], array[idz]])
            else:
                foundSums[sum] = [[array[idx], array[idz]]]

    return out


print(fourNumberSum(array, targetSum))

"""
Input:
[7, 6, 4, -1, 1, 2]
16

Output:
[[7,6,4,-1], [7,6,1,2]]

Idea:
make more efficient than O(n^4) time

loop through all numbers
    loop through all numbers after current
        get difference of targetnumber and sum of numbers
        check if result is in mapping
        if yes: append numbers + mapped pair to output
    loop through all numbers before current
        check if sum of numbers is already mapped
        if yes: add pair
        if no: add number + pair

7:  no mappings yet, first inner for useless; no numbers before, so 2nd inner for useless
6:  no mappings yet, first inner for useless; 6+7=13 -> no mappings -> add 13: [[6,7]]
4:  4+(-1)=3 -> 16-3=13 -> check for mappings -> 13 found -> add [6,7,4,-1] to output
    4+1=5 -> 16-5=11 -> check for mappings -> 11 not found
    4+2=6 -> 16-6=10 -> check for mappings -> 10 not found
    ---
    4+7=11 -> check for mappings -> 11 not found -> add 11: [[4,7]]
    4+6=10 -> check for mappings -> 10 not found -> add 10: [[4,6]]
-1: etc
"""
