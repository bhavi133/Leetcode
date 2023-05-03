Link : https://leetcode.com/problems/permutations-ii/

Code :

import itertools

def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    return list(set(itertools.permutations(nums, len(nums))))
