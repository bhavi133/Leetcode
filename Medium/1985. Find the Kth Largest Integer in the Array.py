Link : https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/

Code :

def kthLargestNumber(self, nums: List[str], k: int) -> str:
    # arr = list(map(int, nums))
    # return str(sorted(arr, reverse=True)[k-1])

    return str(sorted(list(map(int, nums)), reverse=True)[k-1])
