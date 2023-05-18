Link : https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Code :

def searchRange(self, nums, target):
    l = []
    for i in range(len(nums)):
        if nums[i] == target:
            l.append(i)

    if len(l) >= 1:
        return min(l), max(l)
    else:
        return [-1, -1]
