# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        # Write your code here.
        if self.containsNodeWithValue(node.value) and self.containsNode(node):
            if self.head == node:
                return
            self.relinkFormerNeighbors(node)

        formerHead = self.head
        self.head = node
        node.prev = None
        node.next = formerHead
        if formerHead == None:
            self.tail = node
        else:
            formerHead.prev = node

    def setTail(self, node):
        # Write your code here.
        if self.containsNodeWithValue(node.value) and self.containsNode(node):
            if self.tail == node:
                return
            self.relinkFormerNeighbors(node)

        formerTail = self.tail
        self.tail = node
        node.prev = formerTail
        node.next = None
        if formerTail == None:
            self.head = node
        else:
            formerTail.next = node

    def insertBefore(self, node, nodeToInsert):
        # Write your code here.
        if self.containsNode(nodeToInsert):
            self.relinkFormerNeighbors(nodeToInsert)

        prevNode = node.prev
        if prevNode == None:
            self.setHead(nodeToInsert)
            return
        nextNode = node
        prevNode.next = nodeToInsert
        nodeToInsert.prev = prevNode
        nodeToInsert.next = nextNode
        nextNode.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        # Write your code here.
        if self.containsNode(nodeToInsert):
            self.relinkFormerNeighbors(nodeToInsert)

        prevNode = node
        nextNode = node.next
        if nextNode == None:
            self.setTail(nodeToInsert)
            return
        prevNode.next = nodeToInsert
        nodeToInsert.prev = prevNode
        nodeToInsert.next = nextNode
        nextNode.prev = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        # Write your code here.
        if position == 1:
            self.setHead(nodeToInsert)
        else:
            currNode = self.head
            posCounter = 1
            while posCounter != position - 1:
                currNode = currNode.next
                posCounter += 1
            if self.containsNode(nodeToInsert):
                self.relinkFormerNeighbors(nodeToInsert)
            if currNode != nodeToInsert:
                self.insertAfter(currNode, nodeToInsert)
            else:
                self.insertBefore(currNode.next, nodeToInsert)

    def removeNodesWithValue(self, value):
        # Write your code here.
        while self.containsNodeWithValue(value):
            currNode = self.getNodeByValue(value)
            self.remove(currNode)

    def remove(self, node):
        # Write your code here.
        if self.containsNode(node):
            self.relinkFormerNeighbors(node)
            node.prev = None
            node.next = None

    def containsNodeWithValue(self, value):
        # Write your code here.
        currNode = self.head
        while currNode != None:
            if currNode.value == value:
                return True
            currNode = currNode.next
        return False

    def containsNode(self, node):
        currNode = self.head
        while currNode != None:
            if currNode == node:
                return True
            currNode = currNode.next
        return False

    def relinkFormerNeighbors(self, node):
        prevNode = node.prev
        nextNode = node.next
        if prevNode != None:
            prevNode.next = nextNode
        else:
            self.head = nextNode
        if nextNode != None:
            nextNode.prev = prevNode
        else:
            self.tail = prevNode

    def getNodeByValue(self, value):
        currNode = self.head
        while currNode != None:
            if currNode.value == value:
                return currNode
            currNode = currNode.next
        return None
