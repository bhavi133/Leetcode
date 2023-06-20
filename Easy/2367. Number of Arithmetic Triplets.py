Link : https://leetcode.com/problems/number-of-arithmetic-triplets/

Code :

def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
    # count = 0
    # for i in range(len(nums)):
    #     for j in range(i+1, len(nums)):
    #         for k in range(j+1, len(nums)):
    #             if i < j < k and nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
    #                 count += 1
    # return count

    # return len([i for i in range(len(nums)) for j in range(i+1, len(nums)) for k in range(j+1, len(nums)) if i < j < k and nums[j] - nums[i] == diff and nums[k] - nums[j] == diff])

    return len([i for (i, j, k) in itertools.combinations(range(len(nums)), 3) if i < j < k and nums[j] - nums[i] == diff and nums[k] - nums[j] == diff])
