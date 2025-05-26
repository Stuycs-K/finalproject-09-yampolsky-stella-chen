import numpy as np

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
    return [ord(c) - ord('A') for c in text.upper() if c.isalpha()]

def numsToText(nums):
    return ''.join(chr(n % 26 + ord('A')) for n in nums)

def decrypt(text, key):
    invKey = matrixModInverse(key, 26)
    if invKey is None:
        return None
    nums = textToNums(text)
    result = []
    for i in range(0, len(nums), 2):
        pair = np.array(nums[i:i+2]).reshape(2, 1)
        dec = invKey @ pair % 26
        result.extend(dec.flatten())
    return numsToText(result)

if __name__ == "__main__":
    key = np.array([[3, 3], [2, 5]])
    cipher = "ZEBBW"
    plain = decrypt(cipher, key)
    print(plain)
