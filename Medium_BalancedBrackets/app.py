string = "([])(){}(())()()"
string2 = "([])({)}"
string3 = "()())"
string4 = "()()("

def balancedBrackets(string):
    # Write your code here.
    symbols = (("(", "[", "{"), (")", "]", "}"))
    openSymbols = []
    for idx in range(len(string)):
        currChar = string[idx]
        if currChar in symbols[0]:
            openSymbols = [x for x in openSymbols] + [symbols[0].index(currChar)]
        elif currChar in symbols[1]:
            if openSymbols == []:
                return False
            elif symbols[1].index(currChar) == openSymbols[-1]:
                openSymbols.pop(-1)
            else:
                return False
        else:
            continue
    if openSymbols == []:
        return True
    return False


print(balancedBrackets(string))
print(balancedBrackets(string2))
print(balancedBrackets(string3))
print(balancedBrackets(string4))

"""
Input:
string = "([])(){}(())()()"
string2 = "([])({)}"

Output:
True
False
"""