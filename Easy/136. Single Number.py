Link : https://leetcode.com/problems/single-number/

Code :

def singleNumber(self, nums):
    dic = {}
    for i in nums:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    for i, j in dic.items():
        if j == 1:
            return i
