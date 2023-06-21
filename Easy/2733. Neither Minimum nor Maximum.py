Link : https://leetcode.com/problems/neither-minimum-nor-maximum/

Code :

def findNonMinOrMax(self, nums: List[int]) -> int:
    # if len(nums) <= 2:
    #     return -1
    # else:
    #     nums.remove(min(nums))
    #     nums.remove(max(nums))
    #     return nums[0]

    if len(nums) <= 2:
        return -1
    else:
        return sorted(nums)[1]
