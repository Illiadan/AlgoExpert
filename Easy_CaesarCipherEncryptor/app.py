string = "xyz"
key = 2


def caesarCipherEncryptor(string, key):

    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    length = len(alphabet)
    encString = ""
    modKey = key % length
    for str in string:
        str = alphabet[alphabet.index(str) - length + modKey]
        encString += str

    return encString


result = caesarCipherEncryptor(string, key)
print(result)
