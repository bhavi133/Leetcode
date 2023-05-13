Link : https://leetcode.com/problems/strictly-palindromic-number/

Code :

def isStrictlyPalindromic(self, n: int) -> bool:
    return bin(n) == bin(n)[::-1]
