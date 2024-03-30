string = "abcdcaf"


def firstNonRepeatingCharacter(string):

    strSet = set(string)
    out = -1
    for e in strSet:
        if string.count(e) == 1 and out != -1:
            if string.index(e) < out:
                out = string.index(e)
        elif string.count(e) == 1 and out == -1:
            out = string.index(e)

    return out


result = firstNonRepeatingCharacter(string)
print(result)
