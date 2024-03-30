words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp", "aa", "ab"]


def groupAnagrams(words):
    anagrams = {}
    for word in words:
        sortedWord = "".join(sorted(word))
        print(f"word :: {word} // sortedWord :: {sortedWord} // anagrams :: {anagrams}")
        if sortedWord in anagrams:
            anagrams[sortedWord].append(word)
        else:
            anagrams[sortedWord] = [word]
        print(f"word :: {word} // sortedWord :: {sortedWord} // anagrams :: {anagrams}")
    return list(anagrams.values())


print(groupAnagrams(words))
