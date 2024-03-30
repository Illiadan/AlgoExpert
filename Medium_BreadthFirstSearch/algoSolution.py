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
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            array.append(current.name)
            for child in current.children:
                queue.append(child)
        return array
