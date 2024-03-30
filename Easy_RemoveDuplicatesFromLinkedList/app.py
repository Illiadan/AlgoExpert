def removeDuplicatesFromLinkedList(linkedList):
    
    currentNode = linkedList
    while currentNode != None:
        nextDistinctNode = currentNode.next
        while nextDistinctNode != None and nextDistinctNode.value == currentNode.value:
            nextDistinctNode = nextDistinctNode.next
        
        currentNode.next = nextDistinctNode
        currentNode = nextDistinctNode
    
    return linkedList
