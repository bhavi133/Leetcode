Link : https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

Code :

def strStr(self, haystack, needle):
    if needle in haystack:
        return haystack.index(needle)
    else:
        return -1
