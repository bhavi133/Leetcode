Link : https://leetcode.com/problems/median-of-two-sorted-arrays/

Code :

def findMedianSortedArrays(self, nums1, nums2):        
    nums3 = sorted(nums1 + nums2)
    if len(nums3) % 2 == 0:
        median1 = len(nums3) // 2
        median2 = median1 - 1
        return (float(nums3[median1] + nums3[median2])) / 2
    else:
        return nums3[int(len(nums3)/2)]
