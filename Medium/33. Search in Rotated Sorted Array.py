Link : https://leetcode.com/problems/search-in-rotated-sorted-array/

Code :

def search(self, nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    else:
        return -1
