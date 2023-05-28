Link : https://leetcode.com/problems/check-if-n-and-its-double-exist/

Code :

def checkIfExist(self, arr: List[int]) -> bool:
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j and arr[i] == 2 * arr[j]:
                return True
    return False
    
    # s = set()
    # for i in arr:
    #     if i * 2 in s or i / 2 in s:
    #         return True
    #     s.add(i)
    # else:
    #     return False
