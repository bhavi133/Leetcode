Link : https://leetcode.com/problems/permutations/

Code :

import itertools

def permute(self, nums: List[int]) -> List[List[int]]:
    return list(itertools.permutations(nums))
