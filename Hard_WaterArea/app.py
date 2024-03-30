heights = [0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]
heights2 = [0, 1, 1, 0, 0]


def waterArea(heights):
    # Write your code here.
    water = 0
    if len(heights) == 0:
        return water
    globalMax = heights.index(max(heights))
    localMax = globalMax
    while localMax > 0:
        tempMax = heights.index(max(heights[:localMax]))
        if heights[tempMax] == 0:
            break
        else:
            water += (abs(tempMax - localMax) - 1) * heights[tempMax] - sum(
                heights[tempMax + 1 : localMax]
            )
            localMax = tempMax

    localMax = globalMax
    while localMax < len(heights) - 1:
        tempMax = heights.index(max(heights[localMax + 1 :]), localMax + 1)
        if heights[tempMax] == 0:
            break
        else:
            water += (abs(tempMax - localMax) - 1) * heights[tempMax] - sum(
                heights[localMax + 1 : tempMax]
            )
            localMax = tempMax
    return water


print(waterArea(heights2))

"""
Input:
[0,8,0,0,5,0,0,10,0,0,1,1,0,3,0,2]

Output:
48

Idea:
                            |
                            |
    |   .   .   .   .   .   |
    |   .   .   .   .   .   |
    |   .   .   .   .   .   |
    |   .   .   |   .   .   |
    |   .   .   |   .   .   |
    |   .   .   |   .   .   |   .   .   .   .   .   |
    |   .   .   |   .   .   |   .   .   .   .   .   |   .   |
 __ |   .   .   |   .   .   |   .   .   |   |   .   |   .   |
 -> . = trapped Water = 50

array.index(max(array)) -> 7 (=10)
7:  globMax=7, locMax=7
    left check -> while locMax != 0:
    ->  array.index(max(array[:locMax])) -> 1 (=8)
        ->  tempMax=1, water+=(abs(tempMax-locMax)-1)*heights[tempMax]-sum(heights[tempMax+1:locMax])=40-5=35
        ->  locMax=tempMax
    ->  array.index(max(array[:locMax])) -> 0 (=0)
        ->  tempMax=1, if height[tempMax] == 0: break
    locMax=7
    right check -> while locMax != len(heights)-1:
    ->  array.index(max(array[locMax+1:])) -> 13 (=3)
        -> tempMax=13, water=(abs(tempMax-locMax)-1)*heights[tempMax]-sum(heights[locMax+1:tempMax])=35+15-2=48
        -> locMax=tempMax
    ->  array.index(max(array[locMax+1:])) -> 15 (=2)
        -> tempMax=15, water=(abs(tempMax-locMax)-1)*heights[tempMax]-sum(heights[locMax+1:tempMax])=48+2-0=50
        -> locMax=tempMax
-> 50
----
|   .   .   .   .   .   .   .   .   .   |
|   .   |   .   .   .   .   .   |   .   |
|   .   |   .   |   .   .   .   |   .   |
|   .   |   .   |   .   |   .   |   .   |
[4,0,3,0,2,0,1,0,3,0,4] -> 27

array.index(max(array)) -> 0 or 10
0:  -> globMax=0
    left check -> already 0
    right check -> array.index(max(array[globMax+1:])) -> 10
    -> locMax=10
    -> water=(abs(locMax-globMax)-1)*heights[locMax]-sum(heights[globMax+1:locMax])=36-9=27
10: -> globMax=10
    left check -> array.index(max(array[:globMax])) -> 0
    right check -> already len(heights)-1
    -> locMax=0
    -> water=(abs(locMax-globMax)-1)*heights[locMax]-sum(heights[locMax+1:globMax])=36-9=27
"""
