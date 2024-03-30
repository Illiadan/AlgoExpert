class ContinuousMedianHandler:
    def __init__(self):
        # Write your code here.
        self.median = None

    def insert(self, number):
        # Write your code here.
        pass

    def getMedian(self):
        return self.median


cmh = ContinuousMedianHandler()
cmh.insert(5)
cmh.insert(10)
print(cmh.getMedian())
cmh.insert(100)
print(cmh.getMedian())

"""
Input:
continuous insertions of numbers (not sorted)

Output:
median in constant time (O(1) time) with O(log(n) time) for calculating it

Idea:
save insertions in array wont do the trick
-> numbers in array not sorted
-> sorting needs O(n) time

better solution with heaps:
-> build a max heap (for lower half) and a min heap (for greater half)
-> median is the min/max of the set with greater length or average of min and max with equal set length
-> sifting up and down needs O(log(n)) time
-> rearange heaps when length difference is 2
"""
