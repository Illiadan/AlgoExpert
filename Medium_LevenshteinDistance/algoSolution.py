str1 = "abc"
str2 = "yabd"


# O(nm) time | O(min(n,m)) space
def levenshteinDistance(str1, str2):
    """Function takes in two strings and returns the minimum number of edit operations
    that need to be performed on the first string to obtain the second string.
    Edit operations are: insertion of a character, deletion of a character, and
    substitution of a character for another."""
    small = str1 if len(str1) < len(str2) else str2
    big = str1 if len(str1) >= len(str2) else str2
    evenEdits = [x for x in range(len(small) + 1)]
    oddEdits = [None for x in range(len(small) + 1)]
    for i in range(1, len(big) + 1):
        if i % 2 == 1:
            currEdits = oddEdits
            prevEdits = evenEdits
        else:
            currEdits = evenEdits
            prevEdits = oddEdits
        currEdits[0] = i
        for j in range(1, len(small) + 1):
            if big[i - 1] == small[j - 1]:
                currEdits[j] = prevEdits[j - 1]
            else:
                currEdits[j] = 1 + min(prevEdits[j - 1], prevEdits[j],
                                       prevEdits[j - 1])
    return evenEdits[-1] if len(big) % 2 == 0 else oddEdits[-1]


result = levenshteinDistance(str1, str2)
print(result)
