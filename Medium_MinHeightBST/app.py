class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)


def minHeightBst(array):
    """Function takes a non-empty sorted array of integers,
    shall construct minimum height BST from those and returns the BST root."""
    idxList = [_ for _ in range(len(array))]
    rangeList = [[0, len(array) - 1]]
    tree = None
    if len(idxList) is 1:
        tree = BST(array[0])
    else:
        while len(idxList) > 1:
            idx = rangeList[0][0] + (rangeList[0][1] - rangeList[0][0]) // 2
            if idx in idxList:
                if tree is None:
                    tree = BST(array[idx])
                else:
                    tree.insert(array[idx])
                idxList.remove(idx)
                rangeList.append([rangeList[0][0], idx])
                rangeList.append([idx + 1, rangeList[0][1]])
            rangeList.remove(rangeList[0])
        tree.insert(array[idxList[0]])
    return tree


"""
[1,2,5,7,10,13,15,17,22]
n[0]+(n[1]-n[0])//2
[0,8,4] -> 10
[0,4,2] -> 5    |   [5,8,6] -> 15
[0,2,1] -> 2 , [3,4,3] -> 7     |   [5,6,5] -> 13 , [7,8,7] -> 17
[0,1,0] -> 1
"""
