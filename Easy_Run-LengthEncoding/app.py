string = "AAAAAAAAAAAAABBCCCCDD"
string1 = "[(aaaaaaa,bbbbbbb,ccccc,dddddd)]"


def runLengthEncoding(string):

    counter = 0
    out = ""
    for idx in range(len(string)):

        counter += 1
        if idx == len(string) - 1:
            out += encodeString(string[idx], counter)

            return out

        if string[idx] != string[idx + 1]:
            out += encodeString(string[idx], counter)
            counter = 0


def encodeString(string, counter):
    out = ""
    intDiv = counter // 9
    modDiv = counter % 9
    if counter >= 9:
        out += f"9{string}" * (intDiv)
    if modDiv != 0:
        out += f"{modDiv}{string}"

    return out


result = runLengthEncoding(string)
print(result)
