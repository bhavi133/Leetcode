Link : https://leetcode.com/problems/contains-duplicate/

Code :

def containsDuplicate(self, nums):
    # dic = {}
    # l = []
    # for i in nums:
    #     if i in dic:
    #         dic[i] += 1
    #     else:
    #         dic[i] = 1
    # for i, j in dic.items():
    #     if j == 1:
    #         l.append(i)
    # if len(l) > 1:
    #     return True
    # else:
    #     return False

    if len(nums) == len(list(set(nums))):
        return False
    else:
        return True
