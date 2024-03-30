array = [48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41]
"""The task is to implement a MinHeap class that supports:
    -   building the Min Heap from an input array of integers
    -   inserting integers in the heap
    -   removing the heap's root value
    -   peeking at the heap's root value
    -   sifting integers up and down the heap, which is to be used when inserting and removing values
    The heap should be represented by an array.
    MinHeap characteristics:
    -   minimum value is always in the root
    -   not sorted
    -   parent node is always of smaller value than their children
    -   is complete (each row of the tree is filled up from left to right, hence only the last row 
        has potentially fewer nodes than possible)
    """


class MinHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)

    # O(n) time | O(1) space
    def buildHeap(self, array):
        lastIdx = len(array) - 1
        nrOfParents = int(self.floor((lastIdx - 1) / 2)) if lastIdx > 0 else -1
        for parentIdx in range(nrOfParents, -1, -1):
            self.siftDown(array, parentIdx)
        return array

    # O(log(n)) time | O(1) space
    def siftDown(self, heap, idx):
        child1Idx = 2 * idx + 1 if 2 * idx + 1 <= len(heap) - 1 else idx
        child2Idx = 2 * idx + 2 if 2 * idx + 2 <= len(heap) - 1 else idx
        newParentValue = min(heap[idx], heap[child1Idx], heap[child2Idx])
        if newParentValue != heap[idx]:
            childIdx = child1Idx if heap[
                child1Idx] == newParentValue else child2Idx
            heap[idx], heap[childIdx] = newParentValue, heap[idx]
            if 2 * childIdx + 1 <= len(heap) - 1:
                self.siftDown(heap, childIdx)
        return heap

    # O(log(n)) time | O(1) space
    def siftUp(self, heap, idx):
        parentIdx = int(self.floor((idx - 1) / 2))
        newParentValue = min(heap[parentIdx], heap[idx])
        if newParentValue != heap[parentIdx]:
            heap[parentIdx], heap[idx] = newParentValue, heap[parentIdx]
            if parentIdx > 0:
                self.siftUp(heap, parentIdx)
        return heap

    # O(1) time | O(1) space
    def peek(self):
        return self.heap[0]

    # O(log(n)) time | O(1) space
    def remove(self):
        lastIdx = len(self.heap) - 1
        self.heap[0], self.heap[lastIdx] = self.heap[lastIdx], self.heap[0]
        removed = self.heap.pop()
        self.siftDown(self.heap, 0)
        print(self.heap)
        return removed

    # O(log(n)) time | O(1) space
    def insert(self, value):
        self.heap.append(value)
        lastIdx = len(self.heap) - 1
        self.siftUp(self.heap, lastIdx)
        print(self.heap)

    def floor(self, value):
        return value // 1


"""
  0   1   2  3  4   5   6    7   8   9 10 11 12  13
[48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41]
len: 14 -> parents: floor((13-1)/2)=6 [48,12,24,7,8,-5,24]
24: min(24,41) -> [48,12,24,7,8,-5,24,391,24,56,2,6,8,41]
-5: min(-5,6,8) -> [48,12,24,7,8,-5,24,391,24,56,2,6,8,41]
8: min(8,56,2) -> [48,12,24,7,2,-5,24,391,24,56,8,6,8,41]
7: min(7,391,24) -> [48,12,24,7,2,-5,24,391,24,56,8,6,8,41]
24: min(24,-5,24) -> [48,12,-5,7,2,24,24,391,24,56,8,6,8,41] -> min(24,6,8) -> [48,12,-5,7,2,6,24,391,24,56,8,24,8,41]
12: min(12,7,2) -> [48,2,-5,7,12,6,24,391,24,56,8,24,8,41] -> min(12,56,8) -> [48,2,-5,7,8,6,24,391,24,56,12,24,8,41]
48: min(48,2,-5) -> [-5,2,48,7,8,6,24,391,24,56,12,24,8,41] -> min(48,6,24) -> [-5,2,6,7,8,48,24,391,24,56,12,24,8,41]
    -> min(48,24,8) -> [-5,2,6,7,8,8,24,391,24,56,12,24,48,41]
"""
