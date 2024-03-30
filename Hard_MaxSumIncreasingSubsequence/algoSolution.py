array = [10, 70, 20, 30, 50, 11, 30]
array2 = [-1, 1]
array3 = [10, 15, 4, 5, 11, 14, 31, 25, 31, 23, 25, 31, 50]


def maxSumIncreasingSubsequence(array):
    # Write your code here.
    sequences = [None for x in array]
    sums = [num for num in array]
    maxSumIdx = 0
    for idx in range(len(array)):
        currNum = array[idx]
        for jdx in range(0, idx):
            otherNum = array[jdx]
            if otherNum < currNum and sums[jdx] + currNum >= sums[idx]:
                sums[idx] = sums[jdx] + currNum
                sequences[idx] = jdx
        if sums[idx] >= sums[maxSumIdx]:
            maxSumIdx = idx
    return [sums[maxSumIdx], buildSequence(array, sequences, maxSumIdx)]


def buildSequence(array, sequences, currIdx):
    sequence = []
    while currIdx is not None:
        sequence.append(array[currIdx])
        currIdx = sequences[currIdx]
    return list(reversed(sequence))


print(maxSumIncreasingSubsequence(array3))

"""
[10,70,20,30,50,11,30]

seq=[None,None,None,None,None,None,None]
sums=[10,70,20,30,50,11,30]
maxSumIdx=0
0:  10 -> maxSumIdx=0
1:  70 -> 0: 10 -> 10<70&10+70>=70: sums=[10,80,20,30,50,11,30] seq=[None,0,None,None,None,None,None]
       -> maxSumIdx=1
2:  20 -> 0: 10 -> 10<20&10+20>=20: sums=[10,80,30,30,50,11,30] seq=[None,0,0,None,None,None,None]
       -> 1: 70 -> 70>20: sums=[10,80,30,30,50,11,30] seq=[None,0,0,None,None,None,None]
3:  30 -> 0: 10 -> 10<30&10+30>=30: sums=[10,80,30,40,50,11,30] seq=[None,0,0,0,None,None,None]
       -> 1: 70 -> 70>30: sums=[10,80,30,40,50,11,30] seq=[None,0,0,0,None,None,None]
       -> 2: 20 -> 20<30&30+30>=40: sums=[10,80,30,60,50,11,30] seq=[None,0,0,2,None,None,None]
4:  50 -> 0: 10 -> 10<50&10+50>=50: sums=[10,80,30,60,60,11,30] seq=[None,0,0,2,0,None,None]
       -> 1: 70 -> 70>50: sums=[10,80,30,60,60,11,30] seq=[None,0,0,2,0,None,None]
       -> 2: 20 -> 20<50&30+50>=60: sums=[10,80,30,60,80,11,30] seq=[None,0,0,2,2,None,None]
       -> 3: 30 -> 30<50&60+50>=80: sums=[10,80,30,60,110,11,30] seq=[None,0,0,2,3,None,None]
       -> maxSumIdx=4
5:  11 -> 0: 10 -> 10<11&10+11>=11: sums=[10,80,30,60,110,21,30] seq=[None,0,0,2,3,0,None]
6:  30 -> 0: 10 -> 10<30&10+30>=30: sums=[10,80,30,60,110,21,40] seq=[None,0,0,2,3,0,0]
       -> 2: 20 -> 20<30&30+30>=40: sums=[10,80,30,60,110,21,60] seq=[None,0,0,2,3,0,2]
       -> 5: 11 -> 11<30&21+30<60: sums=[10,80,30,60,110,21,60] seq=[None,0,0,2,3,0,2]
-> [4,[10,20,30,50]]
"""
