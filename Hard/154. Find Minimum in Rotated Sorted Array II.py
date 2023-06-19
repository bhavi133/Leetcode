Link : https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

Code :

def findMin(self, nums):
    # return min(nums)

    min = nums[0]
    for i in nums:
        if i <= min:
            min = i
    return min
