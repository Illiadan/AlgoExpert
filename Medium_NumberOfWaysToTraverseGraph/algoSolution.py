width = 4
height = 3


# O(n+m) time | O(1) space
def numberOfWaysToTraverseGraph(width, height):
    """Function takes in two positive integers representing the width and height
    of a grid-shaped, rectangular graph and returns the number of ways to reach
    the bottom-right corner, when starting in the top-left corner.
    Each move can either go right or down."""
    xDistToCorner = width - 1
    yDistToCorner = height - 1
    numerator = factorial(xDistToCorner + yDistToCorner)
    denominator = factorial(xDistToCorner) * factorial(yDistToCorner)
    return numerator // denominator


def factorial(num):
    out = 1
    for n in range(2, num + 1):
        out *= n
    return out


result = numberOfWaysToTraverseGraph(width, height)
print(result)
