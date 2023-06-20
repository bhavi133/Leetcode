Link : https://leetcode.com/problems/number-of-unequal-triplets-in-array/

Code :

def unequalTriplets(self, nums: List[int]) -> int:
    # count = 0
    # for i in range(len(nums)):
    #     for j in range(i+1, len(nums)):
    #         for k in range(j+1, len(nums)):
    #             if nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k]:
    #                 count += 1
    # return count

    # return len([i for i in range(len(nums)) for j in range(i+1, len(nums)) for k in range(j+1, len(nums)) if nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k]])

    return len([i for (i, j, k) in itertools.combinations(range(len(nums)), 3) if nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k]])
