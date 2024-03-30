board = [
    ["t", "h", "i", "s", "i", "s", "a"],
    ["s", "i", "m", "p", "l", "e", "x"],
    ["b", "x", "x", "x", "x", "e", "b"],
    ["x", "o", "g", "g", "l", "x", "o"],
    ["x", "x", "x", "D", "T", "r", "a"],
    ["R", "E", "P", "E", "A", "d", "x"],
    ["x", "x", "x", "x", "x", "x", "x"],
    ["N", "O", "T", "R", "E", "-", "P"],
    ["x", "x", "D", "E", "T", "A", "E"],
]
words = [
    "this",
    "is",
    "not",
    "a",
    "simple",
    "boggle",
    "board",
    "test",
    "REPEATED",
    "NOTRE-PEATED",
]


def boggleBoard(board, words):
    # Write your code here.
    trees = buildWordTrees(words)
    wordsFound = traverseBoard(board, trees)
    return wordsFound


def buildWordTrees(words):
    trees = []
    for word in words:
        currParentSubtree = None
        currSubtree = None
        for idx in range(len(word)):
            if idx == 0:
                currSubtree = checkExistingTrees(trees, word[idx])
                if currSubtree == None:
                    currSubtree = Tree(word[idx])
                    trees.append(currSubtree)
            else:
                currParentSubtree = currSubtree
                currSubtree = checkExistingTrees(currParentSubtree.children, word[idx])
                if currSubtree == None:
                    currSubtree = Tree(word[idx])
                    currParentSubtree.children.append(currSubtree)
        currParentSubtree = currSubtree
        currSubtree = checkExistingTrees(currParentSubtree.children, "*")
        if currSubtree == None:
            currSubtree = Tree("*")
            currParentSubtree.children.append(currSubtree)
    return trees


def checkExistingTrees(listOfTrees, char):
    subtree = None
    for tree in listOfTrees:
        if tree.root == char:
            subtree = tree
            break
    return subtree


class Tree:
    def __init__(self, char):
        self.root = char
        self.children = []


def traverseBoard(board, trees):
    wordsFound = []
    for idx in range(len(board)):
        for idy in range(len(board[0])):
            currSubtree = checkExistingTrees(trees, board[idx][idy])
            if currSubtree != None:
                visited = [[idx, idy]]
                currString = currSubtree.root
                if (
                    checkExistingTrees(currSubtree.children, "*") != None
                    and not currString in wordsFound
                ):
                    wordsFound.append(currString)
                wordsFound = checkPerimeter(
                    board, currSubtree, visited, currString, wordsFound
                )
    return wordsFound


def checkPerimeter(board, tree, visited, currString, wordsFound):
    x = visited[-1][0]
    y = visited[-1][1]
    for idx in range(x - 1, x + 2):
        if idx >= 0 and idx < len(board):
            for idy in range(y - 1, y + 2):
                if idy >= 0 and idy < len(board[0]) and not [idx, idy] in visited:
                    currSubtree = checkExistingTrees(tree.children, board[idx][idy])
                    if currSubtree != None:
                        visited.append([idx, idy])
                        currString += currSubtree.root
                        if (
                            checkExistingTrees(currSubtree.children, "*") != None
                            and not currString in wordsFound
                        ):
                            wordsFound.append(currString)
                        wordsFound = checkPerimeter(
                            board, currSubtree, visited, currString, wordsFound
                        )
                        currString = currString[:-1]
                        visited.pop()
    return wordsFound


print(boggleBoard(board, words))

"""
Input:
[
    ["t", "h", "i", "s", "i", "s", "a"],
    ["s", "i", "m", "p", "l", "e", "x"],
    ["b", "x", "x", "x", "x", "e", "b"],
    ["x", "o", "g", "g", "l", "x", "o"],
    ["x", "x", "x", "D", "T", "r", "a"],
    ["R", "E", "P", "E", "A", "d", "x"],
    ["x", "x", "x", "x", "x", "x", "x"],
    ["N", "O", "T", "R", "E", "-", "P"],
    ["x", "x", "D", "E", "T", "A", "E"]
]
["this", "is", "not", "a", "simple", "boggle", "board", "test", "REPEATED", "NOTRE-PEATED"]

Output:
["this", "is", "a", "simple", "boggle", "board", "NOTRE-PEATED"]

Idea:
divide into 2 problems: board traversing (graph), word matching (tree)

board traversing:

0,0:    t   ->  visited.append(t), t in tree.root for trees
            ->  True:   search around t for matching chars in tree.children until * is hit
            ->  False:  go next

word matching:
    t               b
h       e           o
i       s       a       g
s       t       r       g
*       *       d       l
                *       e
                        *
->  trees = [Tree-t, Tree-b]
    Tree-t: root = "t"
            children = [Tree-h,Tree-e]
"""
