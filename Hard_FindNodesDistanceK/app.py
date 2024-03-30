# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findNodesDistanceK(tree, target, k):
    # Write your code here.
    out = []
    dist = float("-inf")
    found = False
    out, _, _, _ = getNodes(tree, target, k, out, dist, found, None, None)
    return out


def getNodes(node, target, k, out, dist, found, currSubNode, currSubDist):
    if node == None:
        return out, found, currSubNode, currSubDist

    if node.value == target:
        dist = 0
        found = True
        currSubNode = node
        currSubDist = 0
        if dist == k:
            out.append(node.value)
            return out, found, currSubNode, currSubDist

    if not found:
        out, found, currSubNode, currSubDist = getNodes(
            node.left, target, k, out, dist, found, currSubNode, currSubDist
        )
        if not found:
            out, found, currSubNode, currSubDist = getNodes(
                node.right, target, k, out, dist, found, currSubNode, currSubDist
            )
        if found:
            dist = currSubDist + 1
            if dist == k:
                out.append(node.value)
            elif dist < k:
                if node.left == currSubNode:
                    out, found, currSubNode, currSubDist = getNodes(
                        node.right,
                        target,
                        k,
                        out,
                        dist + 1,
                        found,
                        currSubNode,
                        currSubDist,
                    )
                else:
                    out, found, currSubNode, currSubDist = getNodes(
                        node.left,
                        target,
                        k,
                        out,
                        dist + 1,
                        found,
                        currSubNode,
                        currSubDist,
                    )
            currSubNode = node
            currSubDist += 1
            return out, found, currSubNode, currSubDist
    else:
        if dist == k:
            out.append(node.value)
        elif dist > k:
            return out, found, currSubNode, currSubDist
        else:
            out, found, currSubNode, currSubDist = getNodes(
                node.left, target, k, out, dist + 1, found, currSubNode, currSubDist
            )
            out, found, currSubNode, currSubDist = getNodes(
                node.right, target, k, out, dist + 1, found, currSubNode, currSubDist
            )
    return out, found, currSubNode, currSubDist


"""
Input:
target=3
k=2
BT:         1
    2                   3
4       5           6
                7       8

Output:
[2,7,8]

Idea:
(1,0)
(2,-1)
(4,-2)
(5,-2)
(3,1)
(6,2)
(7,3)
(8,3)
-> abs(target[1]-x[1]) == k -> [x[0]]
-------------
k=2
target=8
bt:                     1
            2                       3
    4               5       6               7
8       9

1st check: find target
2nd check: check subtrees with root [target] for nodes in distance k
3rd check: while snapping back increase distance counter and check non-visited subtrees for nodes in distance k

"""
