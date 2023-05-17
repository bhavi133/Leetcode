Link : https://leetcode.com/problems/majority-element/

Code :

def majorityElement(self, nums):
    x = len(nums) // 2
    dic = {}
    l = []
    for i in nums:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    for i, j in dic.items():
        if j > x:
            return i
