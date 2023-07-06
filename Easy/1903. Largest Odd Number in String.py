Link : https://leetcode.com/problems/largest-odd-number-in-string/

Code :

def largestOddNumber(self, num: str) -> str:
    return num.rstrip('02468')
