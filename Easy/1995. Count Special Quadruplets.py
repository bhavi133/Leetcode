Link : https://leetcode.com/problems/count-special-quadruplets/

Code :

def countQuadruplets(self, nums: List[int]) -> int:
    # count = 0
    # for i in range(len(nums)):
    #     for j in range(i+1, len(nums)):
    #         for k in range(j+1, len(nums)):
    #             for l in range(k+1, len(nums)):
    #                 if nums[i] + nums[j] + nums[k] == nums[l]:
    #                     count += 1
    # return count

    # return len([i for i in range(len(nums)) for j in range(i+1, len(nums)) for k in range(j+1, len(nums)) for l in range(k+1, len(nums)) if nums[i] + nums[j] + nums[k] == nums[l]])

    return len([i for (i,j,k,l) in itertools.combinations(range(len(nums)), 4) if nums[i] + nums[j] + nums[k] == nums[l]])
