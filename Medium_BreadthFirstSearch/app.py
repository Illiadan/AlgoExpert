class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    # O(v+e) time | O(v) space
    def breadthFirstSearch(self, array):
        """Node class is given that has optional children nodes. When put
        together, nodes form an acyclic tree-like structure.
        Function takes in an empty array, traverses the tree using the 
        Breadth-first Search approach, stores all the nodes' names in the 
        input array and returns it."""
        return self.breadthFirstTraverse(array, [self])

    def breadthFirstTraverse(self, array, childrenList):
        newChildren = []
        for child in childrenList:
            array.append(child.name)
            newChildren.append(child.children)
        newChildren = [j for i in newChildren for j in i]
        if newChildren != []:
            self.breadthFirstTraverse(array, newChildren)
        return array


"""
A   - B - E
        - F - I
            - J
    - C
    - D - G - K
        - H
[A,B,C,D,E,F,G,H,I,J,K]
"""
