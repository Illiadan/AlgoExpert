class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


# O(n) time | O(n) space
def findSuccessor(tree, node):
    """Function takes in a Binary Tree and a node contained in that tree
    and returns that nodes successor.
    The successor is the next node to be visited when traversing using the 
    in-order traversal technique."""
    out = []
    traverseInOrder(tree, out)
    if node in out and out.index(node) < len(out) - 1:
        return out[out.index(node) + 1]
    return None


def traverseInOrder(tree, out):
    if tree != None:
        traverseInOrder(tree.left, out)
        out.append(tree)
        traverseInOrder(tree.right, out)
    return out
