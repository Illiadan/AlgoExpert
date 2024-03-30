class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        """Function inserts a given value to the BST and returns the BST."""
        nextNode, parentNode, direction = self.nextNode(self, value)
        while nextNode != None:
            nextNode, parentNode, direction = self.nextNode(nextNode, value)
        if direction == -1:
            parentNode.left = BST(value)
        else:
            parentNode.right = BST(value)
        return self

    def contains(self, value):
        """Function checks, if a given value is found in the BST and returns
        True or False respectively."""
        if self.checkNodeValue(self, value):
            return True
        nextNode, parentNode, direction = self.nextNode(self, value)
        while nextNode != None:
            if self.checkNodeValue(nextNode, value):
                return True
            nextNode, parentNode, direction = self.nextNode(nextNode, value)
        return False

    def remove(self, value):
        """Functions removes a given value from the BST, if that BST contains
        more than one node and returns the outcoming BST."""
        if not self.contains(value):
            return self
        nodeToRemove = None
        nodeReplacement = None
        nextNode, parentNode, direction = self, None, 0
        if self.checkNodeValue(self, value):
            if self.left == None and self.right == None:
                return self
            nodeToRemove = self
            parentNode = None
            if self.left == None:
                direction = 1
            else:
                direction = -1
        else:
            nextNode, parentNode, direction = self.nextNode(self, value)
            while nextNode != None:
                if self.checkNodeValue(nextNode, value):
                    nodeToRemove = nextNode
                    break
                nextNode, parentNode, direction = self.nextNode(nextNode, value)
        if nodeToRemove.left == None and nodeToRemove.right == None:
            if direction == -1:
                parentNode.left = None
            else:
                parentNode.right = None
        elif nodeToRemove.left == None:
            if parentNode == None:
                nodeToRemove.value = nodeToRemove.right.value
                nodeToRemove.left = nodeToRemove.right.left
                nodeToRemove.right = nodeToRemove.right.right
            elif direction == -1:
                parentNode.left = nodeToRemove.right
            else:
                parentNode.right = nodeToRemove.right
        elif nodeToRemove.right == None:
            if parentNode == None:
                nodeToRemove.value = nodeToRemove.left.value
                nodeToRemove.right = nodeToRemove.left.right
                nodeToRemove.left = nodeToRemove.left.left
            elif direction == -1:
                parentNode.left = nodeToRemove.left
            else:
                parentNode.right = nodeToRemove.left
        else:
            nodeReplacement, parentNode, direction = self.getNodeReplacement(
                nodeToRemove
            )
            nodeToRemove.value = nodeReplacement.value
            if nodeReplacement.right == None:
                if direction == -1:
                    parentNode.left = None
                else:
                    parentNode.right = None
            else:
                if direction == -1:
                    parentNode.left = nodeReplacement.right
                else:
                    parentNode.right = nodeReplacement.right
        return self

    def nextNode(self, currNode, value):
        if currNode.value <= value:
            return currNode.right, currNode, 1
        else:
            return currNode.left, currNode, -1

    def checkNodeValue(self, currNode, value):
        if currNode.value == value:
            return True
        else:
            return False

    def getNodeReplacement(self, nodeToRemove):
        if nodeToRemove.right == None:
            return nodeToRemove.left
        grandParentNode = nodeToRemove
        parentNode = nodeToRemove.right
        nextNode = nodeToRemove.right.left
        direction = 1
        while nextNode != None:
            direction = -1
            grandParentNode = parentNode
            parentNode = nextNode
            nextNode = nextNode.left
        return parentNode, grandParentNode, direction
