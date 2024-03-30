array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
s1 = [5, 1, 22, 22, 25, 6, -1, 8, 10]

def isValidSubsequence(array, sequence):
    
    indicesList = []
    out = [None, None, array]
    for a in sequence:
        out = listManagement(out[2], a)
        if out[0] == False:
            return False
        else:
            indicesList.append(out[1])

    indicesListSorted = sorted(indicesList)
    if indicesList == indicesListSorted:
        return True
    else:
        return False

def listManagement(list, integer):
    if integer in list:
        ind = list.index(integer)
        list[ind] = None
        return [True, ind, list]
    else:
        return [False]

result = isValidSubsequence(array, sequence)
print(result)
