Link : https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

Code :

def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    return set(set(range(1, len(nums)+1))).difference(set(nums))
