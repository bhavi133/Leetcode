Link : https://leetcode.com/problems/percentage-of-letter-in-string/

Code :

def percentageLetter(self, s: str, letter: str) -> int:
    # count = 0
    # if letter in s:
    #     for i in s:
    #         if i == letter: 
    #             count += 1
    #     return int((count / len(s)) * 100)
    # else:
    #     return 0

    return int((s.count(letter) / len(s)) * 100)
