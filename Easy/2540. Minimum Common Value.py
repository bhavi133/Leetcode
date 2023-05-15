Link : https://leetcode.com/problems/minimum-common-value/

Code :

def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
    # return min(set(nums1) & set(nums2), default=-1)

    l = list(set(nums1).intersection(set(nums2)))
    if len(l) != 0:
        return min(l)
    else:
        return -1
