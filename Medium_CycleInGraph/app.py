edges = [
    [1, 3],
    [2, 3, 4],
    [0],
    [],
    [2, 5],
    [],
]


# O(n^2) time | O(n) space
def cycleInGraph(edges):
    """Function takes in a non-empty two-dimensional list representing outgoing edges 
    in a unweighted, directed graph and returns True if the input list contains cycles 
    otherwise False. A cycle is a connected closed chain of vertices. A vertex is defined 
    by the index in the input list."""
    for i in range(len(edges)):
        revConnections = []
        for j in range(len(edges)):
            if i in edges[j]:
                if i == j:
                    return True
                revConnections.append(j)
        counter = 0
        while revConnections != [] and counter <= len(edges):
            current = revConnections.pop(0)
            for j in range(len(edges)):
                if current in edges[j]:
                    if i == j:
                        return True
                    revConnections.append(j)
            counter += 1
    return False


result = cycleInGraph(edges)
print(result)
"""
0 -> 1,3
1 -> 2,3,4
2 -> 0
3 -> 
4 -> 2,5
5 ->
"""
