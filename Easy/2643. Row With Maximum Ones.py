Link : https://leetcode.com/problems/row-with-maximum-ones/

Code :

def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
    # l = [[i, j.count(1)] for i, j in enumerate(mat)]
    # return sorted(l, reverse=True, key=lambda x : x[1])[0]

    return sorted([[i, j.count(1)] for i, j in enumerate(mat)], reverse=True, key=lambda x : x[1])[0]
