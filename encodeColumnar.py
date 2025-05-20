import sys

def column(plaintext, keyword):
    plaintext = plaintext.replace(" ", "")
    i = 0;
    ciphertext = []
    while i < len(plaintext):
        cipher = []
        for j in range(0, 5):
            if i < len(plaintext):
                cipher.append(plaintext[i])
                i+=1
            else:
                break
        if i < len(plaintext):
            ciphertext.append(cipher)
        else:
            break
    return ciphertext

def columnPrint(doubleArray):
    string = ""
    for i in range(0, len(doubleArray[0])):
        for j in range(0, len(doubleArray)):
            if i < len(doubleArray[j]):
                string += doubleArray[j][i]
            else:
                break
        string+="\n"
    return string

if __name__ == "__main__":
    columnPrint(column(sys.argv[1], sys.argv[2]))
