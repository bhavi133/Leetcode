Link : https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

Code :

def mostWordsFound(self, sentences):
    l = []
    for i in sentences:
        l.append(len(i.split()))
    return max(l)
