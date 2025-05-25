import sys

def column(plaintext, keyword):
    plaintext = plaintext.replace(" ", "")
    i = 0
    ciphertext = []
    while i < len(plaintext):
        cipher = []
        for j in range(0, len(keyword)):
            if i < len(plaintext):
                cipher.append(plaintext[i])
                i+=1
            else:
                break
        ciphertext.append(cipher)
    return ciphertext

def columnPrint(doubleArray):
    string = ""
    for i in range(0, len(doubleArray)):
        for j in range(0, len(doubleArray[0])):
            if j < len(doubleArray[i]):
                string += doubleArray[i][j]
            else:
                break
        string+="\n"
    print(string)

if __name__ == "__main__":
    columnPrint(column(sys.argv[1], sys.argv[2]))
