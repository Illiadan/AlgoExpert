# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(h) time | O(1) space - h is height of BST
def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    # Write your code here.
    if nodeTwo.left == None and nodeTwo.right == None:
        return False
    if isDescendant(nodeTwo, nodeOne):
        if isDescendant(nodeThree, nodeTwo):
            return True
        else:
            return False
    if isDescendant(nodeTwo, nodeThree):
        if isDescendant(nodeOne, nodeTwo):
            return True
        else:
            return False
    return False


def isDescendant(nodeAnc, nodeDesc):
    currNode = nodeAnc
    while currNode != None:
        if nodeDesc.value - currNode.value < 0:
            currNode = currNode.left
            if currNode == nodeDesc:
                return True
        else:
            currNode = currNode.right
            if currNode == nodeDesc:
                return True
    return False


"""
Input:
unknown BST:        5
          2                   7
    1           4       6           8
0           3    
known Nodes:
node1: 5
node2: 2
node3: 3

Output:
True

Idea:
1st check: if node2.left and node2.right == None: return False
2nd check: node1 is desc of node2 
    -> 5 - 2 = 3 -> right -> [4] -> check if node1
    -> 5 - 4 = 1 -> right -> None -> return False
if False: node3 is desc of node2
    -> 3 - 2 = 1 -> right -> [4] -> check if node3
    -> 3 - 4 = -1 -> left -> [3] -> check if node3 -> return True
3rd check: remaining node is anc of node2
    -> 2 - 5 = -3 -> left -> [2] -> check if node2 -> return True
"""
