string = "abaxyzzyxf"
string2 = "abccbait's highnoon"


def longestPalindromicSubstring(string):
    # Write your code here.
    if len(string) == 1:
        return string
    max = ""
    for idx in range(len(string) - 1):
        x = 1
        while (
            idx - x >= 0
            and idx + x < len(string)
            and string[idx - x] == string[idx + x]
        ):
            out = string[idx - x : idx + x + 1]
            if len(out) > len(max):
                max = out
            x += 1
        x = 0
        while (
            idx - x >= 0
            and idx + x + 1 < len(string)
            and string[idx - x] == string[idx + x + 1]
        ):
            out = string[idx - x : idx + x + 2]
            if len(out) > len(max):
                max = out
            x += 1
    return max


print(longestPalindromicSubstring(string))
print(longestPalindromicSubstring(string2))


"""
Input:
"abaxyzzyxf"

Output:
"xyzzyx"

Idea:

"""
