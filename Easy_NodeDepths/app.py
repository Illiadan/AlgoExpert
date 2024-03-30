def nodeDepths(root):

    depths = []
    calculateBranchDepths(root, -1, depths)
    
    return sum(depths)

def calculateBranchDepths(node, currDepth, depths):
    
    if node is None:
        return
    
    runningDepth = currDepth + 1
    depths.append(runningDepth)
    
    calculateBranchDepths(node.left, runningDepth, depths)
    calculateBranchDepths(node.right, runningDepth, depths)
