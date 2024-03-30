array11 = [10, 15, 8, 12, 94, 81, 5, 2, 11]
array12 = [10, 8, 5, 15, 2, 12, 11, 94, 81]


def sameBsts(arrayOne, arrayTwo):
    # Write your code here.
    if (
        len(arrayOne) != len(arrayTwo)
        or arrayOne[0] != arrayTwo[0]
        or len(arrayOne) == 0
        or len(arrayTwo) == 0
    ):
        return False

    left1 = []
    left2 = []
    right1 = []
    right2 = []
    for idx in range(1, len(arrayOne)):
        if arrayOne[idx] < arrayOne[0]:
            left1.append(arrayOne[idx])
        else:
            right1.append(arrayOne[idx])
    for idx in range(1, len(arrayTwo)):
        if arrayTwo[idx] < arrayTwo[0]:
            left2.append(arrayTwo[idx])
        else:
            right2.append(arrayTwo[idx])
    if left1 == left2 and right1 == right2:
        return True
    if left1 != left2:
        outLeft = sameBsts(left1, left2)
    else:
        outLeft = True
    if right1 != right2:
        outRight = sameBsts(right1, right2)
    else:
        outRight = True
    if outLeft and outRight:
        return True
    else:
        return False


print(sameBsts(array11, array12))

"""
Input:
2 arrays -> check if they build same BST, w/o building a BST
[10, 15, 8, 12, 94, 81, 5, 2, 11]
[10, 8, 5, 15, 2, 12, 11, 94, 81]

Output:
True

Idea:
1st check: same length, same element in [0]
-> len: 9 & [10]
2nd check: same elements in left an right subtree
-> left1 = [8,5,2], right1 = [15,12,94,81,11]
-> left2 = [8,5,2], right2 = [15,12,11,94,81]
3rd check: left1 == left2, right1 == right2
4th: start over if left1 != left2 or right1 != right2
-------
1:  len: 5 & [15]
2:  left1: [12,11], right1 = [94,81]
    left2: [12,11], right2 = [94,81]
"""
