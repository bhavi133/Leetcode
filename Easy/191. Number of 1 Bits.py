Link : https://leetcode.com/problems/number-of-1-bits/

Code :

def hammingWeight(self, n: int) -> int:
    # count = 0
    # for i in bin(n)[2:]:
    #     if i == '1':
    #         count += 1
    # return count

    return bin(n)[2:].count('1')
