characters = "Bste!hetsi ogEAxpelrt x "
document = "AlgoExpert is the Best!"


def generateDocument(characters, document):

    charList = list(characters)
    docList = list(document)

    for e in docList:
        if e in charList:
            charList.remove(e)
        else:
            return False

    return True


result = generateDocument(characters, document)
print(result)
