Link : https://leetcode.com/problems/search-a-2d-matrix/

Code :

def searchMatrix(self, matrix, target):
    for i in matrix:
        for j in i:
            if j == target:
                return True
    return False
