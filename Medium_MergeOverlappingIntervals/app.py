intervals = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]


def mergeOverlappingIntervals(intervals):
    """Function takes in a non-empty array of arbitrary intervals, merges
    any overlapping intervals and returns the new intervals in no particular
    order."""
    intervalsSorted = sorted(intervals)
    out = []
    idx = 1
    while idx < len(intervalsSorted):
        if intervalsSorted[idx][0] > intervalsSorted[idx - 1][1]:
            out.append(intervalsSorted[idx - 1])
            if idx == len(intervalsSorted) - 1:
                out.append(intervalsSorted[idx])
        else:
            if intervalsSorted[idx][1] > intervalsSorted[idx - 1][1]:
                intervalsSorted[idx - 1][1] = intervalsSorted[idx][1]
            if idx == len(intervalsSorted) - 1:
                out.append(intervalsSorted[idx - 1])
            intervalsSorted.remove(intervalsSorted[idx])
            idx -= 1
        idx += 1
    return out


result = mergeOverlappingIntervals(intervals)
print(result)
