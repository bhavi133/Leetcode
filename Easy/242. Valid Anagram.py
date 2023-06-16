Link : https://leetcode.com/problems/valid-anagram/

Code :

def isAnagram(self, s, t):
    return sorted(s) == sorted(t)
