class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
    """Function takes in a Binary Search tree and an integer k and
    returns the k-th largest number contained in the BST."""
    out = []
    reverseInOrderTraverse(tree, out, k)
    return out[k - 1]


def reverseInOrderTraverse(tree, array, k):
    if len(array) >= k:
        return array
    if tree != None:
        reverseInOrderTraverse(tree.right, array, k)
        array.append(tree.value)
        reverseInOrderTraverse(tree.left, array, k)
    return array
