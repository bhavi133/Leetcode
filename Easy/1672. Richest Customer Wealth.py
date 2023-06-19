Link : https://leetcode.com/problems/richest-customer-wealth/

Code :

def maximumWealth(self, accounts: List[List[int]]) -> int:
    # l = []
    # for i in accounts:
    #     l.append(sum(i))
    # return max(l)

    return max([sum(i) for i in accounts])
