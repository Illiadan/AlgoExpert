str1 = "ZXVVYZWZ"
str2 = "XKYKZPWZ"


def longestCommonSubsequence(str1, str2):
    # Write your code here.
    out = [["" for x in range(len(str2) + 1)] for y in range(len(str1) + 1)]
    for idx in range(len(str1)):
        for idy in range(len(str2)):
            if str1[idx] == str2[idy]:
                out[idx + 1][idy + 1] = out[idx][idy] + str1[idx]
            else:
                out[idx + 1][idy + 1] = max(
                    out[idx][idy + 1], out[idx + 1][idy], key=lambda x: len(x)
                )
    return [f"{x}" for x in out[len(str1)][len(str2)]]


print(longestCommonSubsequence(str1, str2))

"""
Input:
str1="ZXVVYZWZ"
str2="XKYKZPWZ"

Output:
["X", "Y", "Z", "W", "Z"]

Idea:
    ""  X   K   Y   K   Z   P   W   Z
""  ""  ""  ""  ""  ""  ""  ""  ""  ""
Z   ""  ""  ""  ""  ""  Z   Z   Z   Z
X   ""  X   X   X   X   X   X   X   X
V   ""  X   X   X   X   X   X   X   X
V   ""  X   X   X   X   X   X   X   X
Y   ""  X   X   XY  XY  XY  XY  XY  XY
Z   ""  X   X   XY  XY  XYZ XYZ XYZ XYZ
W   ""  X   X   XY  XY  XYZ XYZ XYZW XYZW
Z   ""  X   X   XY  XY  XYZ XYZ XYZW XYZWZ

------

str1Edit="ZXYZWZ"
str2Edit="XYZWZ"

[[2,4],[0],[1],[2,4],[3],[2,4]]
-> [[2],[4]]
[[2],[4],[0]]
[[2],[4],[0,1]]
[[2],[2,4],[4],[0,1,2],[0,1,4]]
[[2,3],[2,4],[4],[0,1,2,3],[0,1,4]]
[[2,3,4],[2,4],[4],[0,1,2,3,4],[0,1,4],[2]]
......
[[1],[2],[0,3,5],[4],[0,3,5]]
-> [[1]]
[[1,2]]
[[1,2,3],[1,2,5],[0]]
[[1,2,3,4,5],[1,2,5],[0],[0,3],[0,5],[0,4,5]]
----
[0,1,2,3,4,5,6,7]
[[4,7],[0],None,None,[2],[4,7],[6],[4,7]]

[[4],[7]]
[[4],[7],[0]]
[[4],[7],[0],[0,2],[2]]
[[4],[4,7],[7],[0],[0,7],[0,4],[0,4,7],[0,2],[0,2,7],[0,2,4],[0,2,4,7],[2],[2,7],[2,4],[2,4,7]]
[[4],[4,6],[4,7],[7],[0],[0,6],[0,7],[0,4],[0,4,6],[0,4,7],[0,2],[0,2,6],[0,2,7],[0,2,4],[0,2,4,6],[0,2,4,7],[2],[2,6],[2,7],[2,4],[2,4,6],[2,4,7],[6]]
[[4],[4,6],[4,6,7],[4,7],[7],[0],[0,6],[0,6,7],[0,7],[0,4],[0,4,6],[0,4,6,7],[0,4,7],[0,2],[0,2,6],[0,2,6,7],[0,2,7],[0,2,4],[0,2,4,6],[0,2,4,6,7],[0,2,4,7],[2],[2,6],[2,6,7],[2,7],[2,4],[2,4,6],[2,4,6,7],[2,4,7],[6],[6,7]]
-> max(,lambda x: len(x)) -> [0,2,4,6,7]
-> transform from str2
"""
