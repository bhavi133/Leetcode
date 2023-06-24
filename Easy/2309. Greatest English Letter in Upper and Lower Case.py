Link : https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/

Code :

def greatestLetter(self, s: str) -> str:
    # upper = []
    # lower = []
    # for i in s:
    #     if i.isupper():
    #         upper.append(i)
    #     else:
    #         lower.append(i)
    # l = []
    # for i in s:
    #     if i.upper() in upper and i.lower() in lower and i not in l:
    #         l.append(i.upper())

    # if len(l) != 0:
    #     return sorted(list(set(l)), reverse=True)[0]
    # else:
    #     return ""

    l = set()
    for i in s:
        if i.isupper():
            if i.lower() in s:
                l.add(i)
    
    if len(l) != 0:
        return max(list(l))
    else:
        return ""
