Link : https://leetcode.com/problems/search-insert-position/

Code :

def searchInsert(self, nums, target):
    for i in nums:
        if i == target:
            return nums.index(i)
        else:
            nums.append(target)
            return sorted(nums).index(target)
