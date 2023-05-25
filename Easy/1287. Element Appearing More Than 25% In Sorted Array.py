Link : https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/

Code :

import collections

def findSpecialInteger(self, arr: List[int]) -> int:
    # dic = collections.Counter(arr)
    # x = len(arr) * 0.25
    # for i, j in dic.items():
    #     if j > x:
    #         return i

    dic = collections.Counter(arr)
    for i, j in dic.items():
        if j > len(arr) // 4:
            return i
