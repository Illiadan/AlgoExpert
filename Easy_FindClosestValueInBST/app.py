{
  "target": 12,
  "tree": {
    "nodes": [
      {"id": "10", "left": "5", "right": "15", "value": 10},
      {"id": "15", "left": "13", "right": "22", "value": 15},
      {"id": "22", "left": null, "right": null, "value": 22},
      {"id": "13", "left": null, "right": "14", "value": 13},
      {"id": "14", "left": null, "right": null, "value": 14},
      {"id": "5", "left": "2", "right": "5-2", "value": 5},
      {"id": "5-2", "left": null, "right": null, "value": 5},
      {"id": "2", "left": "1", "right": null, "value": 2},
      {"id": "1", "left": null, "right": null, "value": 1}
    ],
    "root": "10"
  }
}

tree = [
    [10, 5, 15],
    [15, 13, 22],
    [22, None, None],
    [13, None, 14],
    [14, None, None],
    [5, 2, 5],
    [5, None, None],
    [2, 1, None],
    [1, None, None],
]
target = 12

def findClosestValueInBst(tree, target):
    """Function that takes in a Binary Search Tree (BST) and a target integer value and returns the closest value
    to that target value contaqined in the BST"""

    out = [None, None]
    node = tree

    while node != None:

        if node.value == target:
            return node.value
		
        res = getNextBSTNode(node, target, out)
        out = res[1]
        node = res[0]
	
	if abs(out[0] - target) < abs(out[1] - target):
	    return out[0]
	else:
        return out[1]

def getNextBSTNode(node, target, out):

    nextNode = None
    if node.value < target:
        out[0] = node.value
        nextNode = node.right
    else:
        out[1] = node.value
        nextNode = node.left
    
    return [nextNode, out]

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


result = findClosestValueBST(tree, target)
print(result)
