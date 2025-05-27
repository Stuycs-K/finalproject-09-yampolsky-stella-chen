import sys

def column(plaintext, keyword):
    plaintext = plaintext.replace(" ", "")
    plaintext = plaintext.replace(",","")
    plaintext = plaintext.replace(".","")
    plaintext = plaintext.replace("?","")
    plaintext = plaintext.replace("!","")
    plaintext = plaintext.replace("(","")
    plaintext = plaintext.replace(")","")
    i = 0
    ciphertext = []
    while i < len(plaintext):
        cipher = []
        for j in range(0, len(keyword)):
            if i < len(plaintext):
                cipher.append(plaintext[i])
                i+=1
            else:
                cipher.append(" ")
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
        if i != len(doubleArray)-1:
            string+="\n"
    print(string)
    
def cipherTextPrint(doubleArray):
    array = []
    for i in doubleArray:
        for j in i:
            array.append(j)
    print("".join(array))

def swap(doubleArray, keyword):
    cipher = []
    keywordSorted = sorted(list(keyword))
    keyword = list(keyword)
    for i in range(0, len(doubleArray)):
        cipher.append([])
    for i in keywordSorted:
        index = keyword.index(i)
        for j in range(0, len(doubleArray)):
            cipher[j].append(doubleArray[j][index])
    return cipher

if __name__ == "__main__":
    if (sys.argv[3] == "column" or sys.argv[3] == "Column"):
        columnPrint(swap(column(sys.argv[1], sys.argv[2]), sys.argv[2]))
    elif (sys.argv[3] == "linear" or sys.argv[3] == "Linear"):
        cipherTextPrint(swap(column(sys.argv[1], sys.argv[2]), sys.argv[2]))

