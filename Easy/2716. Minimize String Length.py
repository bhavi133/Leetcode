Link : https://leetcode.com/problems/minimize-string-length/

Code :

def minimizedStringLength(self, s: str) -> int:
    # return len(set(s))
    return len(list(set(s)))
