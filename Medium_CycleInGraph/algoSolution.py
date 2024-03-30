edges = [
    [1, 3],
    [2, 3, 4],
    [0],
    [],
    [2, 5],
    [],
]


# O(v+e) time | O(v) space
def cycleInGraph(edges):
    """Function takes in a non-empty two-dimensional list representing outgoing edges 
    in a unweighted, directed graph and returns True if the input list contains cycles 
    otherwise False. A cycle is a connected closed chain of vertices. A vertex is defined 
    by the index in the input list."""
    visited = [0 for i in range(len(edges))]
    inStack = [0 for i in range(len(edges))]

    for node in range(len(edges)):
        if visited[node]:
            continue

        containsCycle = isNodeInCycle(node, edges, visited, inStack)
        if containsCycle:
            return True


def isNodeInCycle(node, edges, visited, inStack):
    visited[node] = True
    inStack[node] = True

    neighbors = edges[node]
    for neighbor in neighbors:
        if not visited[neighbor]:
            containsCycle = isNodeInCycle(neighbor, edges, visited, inStack)
            if containsCycle:
                return True
        elif inStack[neighbor]:
            return True

    inStack[node] = False
    return False


result = cycleInGraph(edges)
print(result)
