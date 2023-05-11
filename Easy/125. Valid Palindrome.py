Link : https://leetcode.com/problems/valid-palindrome/

Code :

def isPalindrome(self, s: str) -> bool:
    l = ''.join(i for i in s if i.isalnum())
    return l.lower() == l[::-1].lower()
