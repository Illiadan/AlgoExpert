class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    """Funtion takes in a Binary Tree and returns it's diameter.
    Diameter of a BT is length of longest path.
    Path is collection of connected nodes, where no node is connected to more than two nodes."""
    _, maxCounter = binaryTreeDiameterHelper(tree, 0, 0, 0)
    return maxCounter


def binaryTreeDiameterHelper(tree, leftCounter, rightCounter, maxCounter):
    newLeftCounter = 0
    newRightCounter = 0
    if tree.left != None:
        newLeftCounter, maxCounter = binaryTreeDiameterHelper(
            tree.left, leftCounter, rightCounter, maxCounter)
        newLeftCounter += 1
    if tree.right != None:
        newRightCounter, maxCounter = binaryTreeDiameterHelper(
            tree.right, leftCounter, rightCounter, maxCounter)
        newRightCounter += 1
    # if leftCounter + newLeftCounter + rightCounter + newRightCounter > maxCounter:
    #    maxCounter = leftCounter + newLeftCounter + rightCounter + newRightCounter
    maxCounter = max(
        leftCounter + newLeftCounter + rightCounter + newRightCounter,
        maxCounter)
    # if newLeftCounter > newRightCounter:
    #    return newLeftCounter, maxCounter
    # return newRightCounter, maxCounter
    return max(newLeftCounter, newRightCounter), maxCounter


"""
def binaryTreeDiameter(tree):
    _, maxCounter = binaryTreeDiameterHelper(tree, 0, 0, 0)
    return maxCounter

def binaryTreeDiameterHelper(tree, leftCounter, rightCounter, maxCounter):
    newLeftCounter = 0
    newRightCounter = 0
    while tree.left != None:
        newLeftCounter, maxCounter = binaryTreeDiameter(tree.left, leftCounter, rightCounter, maxCounter)
        newLeftCounter += 1
    while tree.right != None:
        newRightCounter, maxCounter = binaryTreeDiameter(tree.right, leftCounter, rightCounter, maxCounter)
        newRightCounter += 1
    if leftCounter + newLeftCounter + rightCounter + newRightCounter > maxCounter:
        maxCounter = leftCounter + newLeftCounter + rightCounter + newRightCounter
    if newLeftCounter > newRightCounter:
        return newLeftCounter, maxCounter
    return newRightCounter, maxCounter

1,0,0,0
    3,0,0,0
        7,0,0,0
            8,0,0,0
                9,0,0,0
                return 0,0
            l = 1
            1>0:
            m = 1
            return 1,1
        l = 2
        2>1:
        m = 2
        return 2,2
    l=3
        4,0,0,2
            5,0,0,2
                6,0,0,2
                return 0,2
            r=1
            return 1,2
        r=2
        return 2,2
    r=3
    6>2:
    m=6
    return 3,6
l=4
    2,0,0,6
    return 0,6
r=1
return 4,6
        
"""
