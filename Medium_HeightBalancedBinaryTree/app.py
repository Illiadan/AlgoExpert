class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n) time | O(h) space
def heightBalancedBinaryTree(tree):
    """Function takes ion the root of a Binary Tree and returns True if
    this BT is height balanced.
    A BT is height balanced, if for each node in the tree the difference 
    between the height of the left subtree and the right subtree is at most 1."""
    _, maxHeightDiff = getSubtreeHeight(tree, 0, 0, 0)
    if maxHeightDiff > 1:
        return False
    return True


def getSubtreeHeight(tree, heightLeftSubtree, heightRightSubtree,
                     maxHeightDiff):
    newHeightLeftSubtree = 0
    newHeightRightSubtree = 0
    if tree.left != None:
        newHeightLeftSubtree, maxHeightDiff = getSubtreeHeight(
            tree.left, heightLeftSubtree, heightRightSubtree, maxHeightDiff)
        newHeightLeftSubtree += 1
    if tree.right != None:
        newHeightRightSubtree, maxHeightDiff = getSubtreeHeight(
            tree.right, heightLeftSubtree, heightRightSubtree, maxHeightDiff)
        newHeightRightSubtree += 1
    maxHeightDiff = max(
        abs(heightLeftSubtree + newHeightLeftSubtree - heightRightSubtree -
            newHeightRightSubtree), maxHeightDiff)
    return max(newHeightLeftSubtree, newHeightRightSubtree), maxHeightDiff
