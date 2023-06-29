Link : https://leetcode.com/problems/two-out-of-three/

Code :

def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
    # l = list(set(nums1)) + list(set(nums2)) + list(set(nums3))
    # x = []
    # for i in l:
    #     if l.count(i) >= 2 and i not in x:
    #         x.append(i)
    # return x

    l1 = list(set(nums1).intersection(set(nums2)))
    l2 = list(set(nums2).intersection(set(nums3)))
    l3 = list(set(nums1).intersection(set(nums3)))
    return list(set(l1 + l2 + l3))
