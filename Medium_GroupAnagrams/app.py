words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp", "aa", "ab"]


def groupAnagrams(words):
    # Write your code here.
    out = []
    while len(words) > 0:
        popped = [words.pop(0)]
        query = words.copy()
        print(f"popped :: {popped} // query :: {query}")
        while len(query) != 0:
            print(f"element :: {query[0]} // query :: {query} // words :: {words}")
            if len(query[0]) != len(popped[0]):
                query.remove(query[0])
                continue
            value = str(query[0])
            for char in popped[0]:
                print(f"char :: {char} // value :: {value} // query[0] :: {query[0]}")
                if char in value:
                    value = value.replace(char, "", 1)
                else:
                    query.remove(query[0])
                    break
            if len(value) == 0:
                popped.append(query[0])
                words.remove(query[0])
                query.remove(query[0])
        out.append(popped)
    return out


print(groupAnagrams(words))

"""
Input:
["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]

Output:
[["yo", "oy"], ["flop", "olfp"], ["act", "tac", "cat"], ["foo"]]

Idea:
pop()
query [words] for length of pop()
check query for each character of pop() and create new resolving query after each character
break if query is empty
[pop() + remaining query] is output
remove remaining query elements from [words]
return output when [words] is empty
"""
