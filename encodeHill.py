import numpy as np

def textToNums(text):
    return [ord(c) - ord('A') for c in text.upper() if c.isalpha()]

def numsToText(nums):
    return ''.join(chr(n % 26 + ord('A')) for n in nums)