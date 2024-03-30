class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        # Write your code here.
        self.depthFirstSearchHelper(array)

        return array

    def depthFirstSearchHelper(self, array):
        
        array.append(self.name)
        for node in self.children:
            node.depthFirstSearchHelper(array)
