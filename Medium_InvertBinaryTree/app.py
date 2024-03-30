class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def invertBinaryTree(tree):
    """Function takes in a Binary Tree, inverts it and returns the inverted BT"""
    if tree != None:
        tree.left, tree.right = tree.right, tree.left
        invertBinaryTree(tree.left)
        invertBinaryTree(tree.right)
    return tree
