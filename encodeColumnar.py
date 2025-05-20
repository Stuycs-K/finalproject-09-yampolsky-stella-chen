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

if __name__ == "__main__":
    print(column(sys.argv[1], sys.argv[2]))
