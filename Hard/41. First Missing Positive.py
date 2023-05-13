Link : https://leetcode.com/problems/first-missing-positive/

Code :

def firstMissingPositive(self, nums: List[int]) -> int:
    l = set(nums)
    for i in range(1, len(nums)+2):
        if i not in l:
            return i
