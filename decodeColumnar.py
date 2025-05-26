import sys
import math

def decode(ciphertext, keyword):
    plaintext = []
    keywordSorted = sorted(list(keyword))
    keyword = list(keyword)
    cipher = []
    for i in range(0, math.floor(len(ciphertext)/len(keyword))):
        plaintext.append([])
        cipher.append([])
    a = 0
    i = 0
    while i < len(ciphertext):
        for j in range(0, math.floor(len(ciphertext)/len(keyword))):
            cipher[a].append(ciphertext[i])
            i+=1
        a+=1
    for b in keyword:
        index = keywordSorted.index(b)
        for c in range(0, len(cipher)):
            plaintext[c].append(cipher[c][index])
    plain = []
    for x in plaintext:
        plain.append("".join(x))
    return "".join(plain)

if __name__ == "__main__":
    print(decode(sys.argv[1], sys.argv[2]))