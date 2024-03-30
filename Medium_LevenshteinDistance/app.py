str1 = "abc"
str2 = "yabd"


# O(nm) time | O(nm) space
def levenshteinDistance(str1, str2):
    """Function takes in two strings and returns the minimum number of edit operations
    that need to be performed on the first string to obtain the second string.
    Edit operations are: insertion of a character, deletion of a character, and
    substitution of a character for another."""
    editsTable = [[y for y in range(len(str2) + 1)]
                  for x in range(len(str1) + 1)]
    for i in range(1, len(str1) + 1):
        editsTable[i][0] = editsTable[i - 1][0] + 1
    for rowIdx in range(1, len(editsTable)):
        for colIdx in range(1, len(editsTable[rowIdx])):
            if str1[rowIdx - 1] == str2[colIdx - 1]:
                editsTable[rowIdx][colIdx] = editsTable[rowIdx - 1][colIdx - 1]
            else:
                editsTable[rowIdx][colIdx] = min(
                    editsTable[rowIdx][colIdx - 1],
                    editsTable[rowIdx - 1][colIdx - 1],
                    editsTable[rowIdx - 1][colIdx]) + 1
    return editsTable[-1][-1]


result = levenshteinDistance(str1, str2)
print(result)
"""
abc | yabd
    ""  y   a   b   d
""  0   1   2   3   4
a   1   1   1   2   3
b   2   2   2   1   2
c   3   3   3   2   2

if str1[r] == str2[c]:
    E[r][c]=E[r-1][c-1]
else:
    E[r][c]=min(E[r][c-1],E[r-1][c-1],E[r-1][c])+1
"""
