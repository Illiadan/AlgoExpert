words = ["this", "that", "did", "deed", "them!", "a"]


def minimumCharactersForWords(words):
    # Write your code here.
    chars = {}
    for word in words:
        for char in word:
            x = word.count(char)
            if char not in chars:
                chars[char] = x
            elif chars[char] < x:
                chars[char] = x
    out = []
    for key in chars.keys():
        for y in range(chars[key]):
            out.append(key)
    return out


print(minimumCharactersForWords(words))

"""
Input:
["this", "that", "did", "deed", "them!", "a"]

Output:
["t", "t", "h", "i", "s", "a", "d", "d", "e", "e", "m", "!"]

Idea:
hist
ahtt
ddi
ddee
ehmt!
a
"""
