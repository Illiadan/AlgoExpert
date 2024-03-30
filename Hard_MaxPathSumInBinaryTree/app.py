def maxPathSum(tree):
    # Write your code here.
    out = calcPathSums(tree)
    return max(out)


def calcPathSums(node):
    left = (float("-inf"), float("-inf"))
    right = (float("-inf"), float("-inf"))
    root = node.value

    if node.left != None:
        left = calcPathSums(node.left)
    if node.right != None:
        right = calcPathSums(node.right)

    leftLine = left[0]
    leftOverall = left[1]
    rightLine = right[0]
    rightOverall = right[1]
    subMax = max(leftLine, rightLine)
    lineMax = max(subMax + root, root)
    overallMax = max(leftOverall, rightOverall, leftLine + root + rightLine, lineMax)
    print(f"{root}: ({lineMax},{overallMax})")
    return (lineMax, overallMax)


"""
Input:
Binary Tree
            1
    2               3
4       5       6       7

            1
    -5              3
6

            -100
    2               3
4       5       6       7

Output:
18 (5+2+1+3+7)

Idea:
1st: maximum can be anywhere (not necessarilly connected to root)
2nd: path can be a line or a triangle

recursion:  left child == None, right child == None
1st check:  LeftMax: maximum left side as line, LSO: maximum left side overall
2nd check:  RightMax: maximum right side as line, RSO: maximum right side overall
3rd check:  SubMax: maximum left side line and right side line
4th check:  LineMax: maximum SubMax + root and root
5th check:  TriangleMax: maximum LSO and RSO and LeftMax + Root + RightMax
return (LineMax, TriangleMax)
return max(lastTuple)

4 -> LM: None, LSO: None, RM: None, RSO: None, SM: None, LM: 4; TM: 4 -> (4,4)
5 -> (5,5)
2 -> LM: 4, LSO: 4, RM: 5, RSO: 5, SM: 5, LM: 7; TM: 11 -> (7,11)
6 -> (6,6)
7 -> (7,7)
3 -> LM: 6, LSO: 6, RM: 7, RSO: 7, SM: 7, LM: 10; TM: 16 -> (10,16)
1 -> LM: 7, LSO: 11, RM: 10, RSO: 16, SM: 10, LM: 11; TM: 18 -> (11,18)
-> 18
"""
