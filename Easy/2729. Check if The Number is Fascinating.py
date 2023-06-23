Link : https://leetcode.com/problems/check-if-the-number-is-fascinating/

Code :

def isFascinating(self, n: int) -> bool:
    # s = list("123456789")
    # x = 2 * n
    # y = 3 * n
    # z = str(n) + str(x) + str(y)
    # return sorted(z) == s

    return sorted(str(n)+str(2*n)+str(3*n)) == list("123456789")
