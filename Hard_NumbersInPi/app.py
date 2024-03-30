pi = "3141592653589793238462643383279"
numbers = [
    "314159265358979323846",
    "26433",
    "8",
    "3279",
    "314159265",
    "35897932384626433832",
    "79",
]
pi2 = "3141592"
numbers2 = ["3141", "5", "31", "2", "4159", "9", "42"]


def numbersInPi(pi, numbers):
    # Write your code here.
    spaces = {}
    getSpaces(pi, numbers, spaces)
    print(spaces)
    return spaces[pi] if pi in spaces.keys() else -1


def getSpaces(currNumber, numbers, spaces):
    for idx in range(len(currNumber)):
        if currNumber[0 : idx + 1] in spaces.keys():
            if (
                spaces[currNumber[0 : idx + 1]] != 0
                and currNumber[0 : idx + 1] in numbers
            ):
                spaces[currNumber[0 : idx + 1]] = 0
            return
        if currNumber[0 : idx + 1] in numbers:
            if len(currNumber[idx + 1 :]) == 0:
                spaces[currNumber[0 : idx + 1]] = 0
            else:
                getSpaces(currNumber[idx + 1 :], numbers, spaces)
                if currNumber[idx + 1 :] in spaces.keys():
                    if currNumber in spaces.keys():
                        spaces[currNumber] = min(
                            spaces[currNumber], spaces[currNumber[idx + 1 :]] + 1
                        )
                    else:
                        spaces[currNumber] = spaces[currNumber[idx + 1 :]] + 1


print(numbersInPi(pi, numbers))

"""
Input:
"3141592"
["3141","5","31","2","4159","9","42"]

"3141592653589793238462643383279"
["314159265358979323846", "26433", "8", "3279", "314159265", "35897932384626433832", "79"]

Output:
2

Idea:
pi needs to be parted in a way that all outcoming parts are in numbers
-> need min of parts

"3141592"
["3141","5","31","2","4159","9","42"]

3: False
31: True
    ->  4:  False
        41: False
        415:    False
        4159:   True
        ->  2:  True
            ->  add 2 to dict with value 0
        ->  add 41592 to dict with value 1
        41592:  False
    ->  add 3141592 to dict with value 2
314:    False
3141:   True
    ->  5:  True
        ->  9:  True
            ->  2:  found in dict with value 0
        ->  add 92 to dict with value 1
        -> 92:  False
    ->  add 592 to dict with value 2
    ->  59: False
    ->  592:    False
    ->  3141592:    3 > 2 -> do nothing
31415:  False
314159: False
3141592:    False 

"""
