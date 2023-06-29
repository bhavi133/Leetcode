Link : https://leetcode.com/problems/find-smallest-letter-greater-than-target/

Code :

def nextGreatestLetter(self, letters: List[str], target: str) -> str:
    # l = [ord(i) for i in letters]
    # target = ord(target)
    # for i in l:
    #     if i > target:
    #         return letters[l.index(i)]
    # else:
    #     return letters[0]

    for i in letters:
        if i > target:
            return i
    return letters[0]
