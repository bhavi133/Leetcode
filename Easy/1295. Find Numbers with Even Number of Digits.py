Link : https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

Code :

def findNumbers(self, nums: List[int]) -> int:
    # return len([i for i in nums if len(str(i)) % 2 == 0])

    count = 0
    for i in nums:
        if len(str(i)) % 2 == 0:
            count += 1
    return count
