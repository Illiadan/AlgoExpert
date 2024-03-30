array = [1, 2, 3, 5, 6, 8, 9]

def sortedSquaredArray(array):

    out = []
    for a in array:
        out.append(a*a)
    out = sorted(out)
    
    return out

result = sortedSquaredArray(array)
print(result)
