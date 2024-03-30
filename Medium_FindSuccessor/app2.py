class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


# O(h) time | O(1) space
def findSuccessor(tree, node):
    """Function takes in a Binary Tree and a node contained in that tree
    and returns that nodes successor.
    The successor is the next node to be visited when traversing using the 
    in-order traversal technique."""
    if node.right != None:
        out = node.right
        while out.left != None:
            out = out.left
        return out
    curr = node
    out = node.parent
    while out != None:
        if curr == out.left:
            return out
        out = out.parent
        curr = curr.parent
    return None
