def branchSums(root):
    # Write your code here.
    tempSum = 0
    nodes = [{"node": root, "sum": tempSum}]
    out = []
    isNone = False

    while nodes != []:
	    obj = getNextNode(nodes[0]["node"], nodes[0]["sum"], True)
	    if obj["node"] == None:
		    isNone = True
	    else:
		    nodes.insert(1, obj)
	    obj = getNextNode(nodes[0]["node"], nodes[0]["sum"], False)
	    nodes.remove(nodes[0])
	    if obj["node"] == None and isNone == True:
		    out.append(obj["sum"])
	    elif obj["node"] != None:
		    nodes.insert(1, obj)
	    isNone = False
		
    return out

def getNextNode(node, tempSum, isLeft):

    tempSum += node.value
    if isLeft:
        left = node.left
        return {"node": left, "sum": tempSum}
    else:
        right = node.right
        return {"node": right, "sum": tempSum}
