import numpy as np
import sys
char_dict = {
    "_": 0, "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9,
    "J": 10, "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18,
    "S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26,
    "0": 27, "1": 28, "2": 29, "3": 30, "4": 31, "5": 32, "6": 33, "7": 34, "8": 35, "9": 36,
    ".": 37, "?": 38, ",": 39, "-": 40
}

def modInverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def matrixModInverse(matrix, modulus):
    det = int(np.round(np.linalg.det(matrix)))
    detInv = modInverse(det % modulus, modulus)
    if detInv is None:
        return None
    adj = np.round(det * np.linalg.inv(matrix)).astype(int) % modulus
    return (detInv * adj) % modulus

def textToNums(text):
    return [char_dict(c) for c in text.upper() if c.isalpha()]

def numsToText(nums):
    return ''.join([key for key, val in char_dict.items() if val == n] for n in nums)

def decrypt(text, key):
    invKey = matrixModInverse(key, 41)
    if invKey is None:
        return ""
    nums = textToNums(text)
    if len(nums) % 2 != 0:
        nums.append(0)
    result = []
    for i in range(0, len(nums), 2):
        pair = np.array(nums[i:i+2]).reshape(2, 1)
        dec = invKey @ pair % 41
        result.extend(dec.flatten())
    output = numsToText(result)
    return output.rstrip('A')  # Remove potential padding



if __name__ == "__main__":
    text = sys.argv[1]
    keyValues = list(map(int, sys.argv[2].split(',')))
    key = np.array(keyValues).reshape(2, 2)
    print(decrypt(text, key))
