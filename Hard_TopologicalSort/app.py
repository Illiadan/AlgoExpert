jobs = [1, 2, 3, 4]
deps = [[1, 2], [1, 3], [3, 2], [4, 2], [4, 3]]

jobs2 = [1, 2, 3, 4, 5]
deps2 = [[1, 2], [1, 3], [3, 2], [4, 2], [4, 3]]

jobs3 = [1, 2, 3, 4]
deps3 = [[1, 2], [1, 3], [3, 2], [4, 2], [4, 3], [2, 4]]

jobs4 = [1, 2, 3, 4, 5]
deps4 = [[5, 2], [5, 3], [3, 2], [4, 2], [4, 3]]

jobs5 = [1, 2, 3, 4, 5, 6, 7, 8]
deps5 = [[3, 1], [8, 1], [8, 7], [5, 7], [5, 2], [1, 4], [6, 7], [1, 2], [7, 6]]


def topologicalSort(jobs, deps):
    # Write your code here.
    out = []
    visited = []
    visiting = []
    invalid = False
    for x in jobs:
        out, visited, visiting, invalid = topologicalSortHelper(
            x, deps, out, visited, visiting, invalid
        )
    return out


def topologicalSortHelper(currNumber, deps, out, visited, visiting, invalid):
    if invalid or isVisiting(currNumber, visiting):
        out = []
        invalid = True
        return out, visited, visiting, invalid
    if isVisited(currNumber, visited):
        return out, visited, visiting, invalid

    visiting.append(currNumber)
    preNumbers = prerequisitesCheck(currNumber, deps)
    if len(preNumbers) != 0:
        for x in preNumbers:
            out, visited, visiting, invalid = topologicalSortHelper(
                x, deps, out, visited, visiting, invalid
            )
    out.append(currNumber)
    visiting.pop()
    visited.append(currNumber)
    return out, visited, visiting, invalid


def isVisiting(currNumber, visiting):
    return currNumber in visiting


def isVisited(currNumber, visited):
    return currNumber in visited


def prerequisitesCheck(currNumber, deps):
    preNumbers = []
    for x in deps:
        if currNumber == x[1]:
            preNumbers.append(x[0])
    return preNumbers


print(topologicalSort(jobs5, deps5))

"""
Input:
jobs = [1,2,3,4]
deps = [[1,2],[1,3],[3,2],[4,2],[4,3]]

Output:
[1,4,3,2] or [4,1,3,2]

Idea:
for all jobs check if each has prerequisites
-> if not and job not already in output -> add to output else: follow prerequisite or continue

out = []
1:  no prereq. and not in out
->  out = [1]
2:  prereq.
    -> 1:   in out
    -> 3:   prereq.
            ->  1:  in out
            ->  4:  no prereq. and not in out
                ->  out = [1,4]
        ->  out = [1,4,3]
    -> 4:   in out
->  out = [1,4,3,2]
3:  in out
4:  in out 
"""
