import numpy as np

def textToNums(text):
    return [ord(c) - ord('A') for c in text.upper() if c.isalpha()]

def numsToText(nums):
    return ''.join(chr(n % 26 + ord('A')) for n in nums)

def encrypt(text, key):
    nums = textToNums(text)
    if len(nums) % 2 != 0:
        nums.append(0)
    result = []
    for i in range(0, len(nums), 2):
        pair = np.array(nums[i:i+2]).reshape(2, 1)
        enc = key @ pair % 26
        result.extend(enc.flatten())
    return numsToText(result)