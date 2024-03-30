string = "abcdcba"


def isPalindrome(string):

    idx = 0
    jdx = len(string) - 1
    while idx < jdx:
        if string[idx] != string[jdx]:
            return False
        idx += 1
        jdx -= 1
    return True


result = isPalindrome(string)
print(result)
